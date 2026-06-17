package handlers

import (
	"encoding/json"
	"net/http"

	"github.com/go-chi/chi/v5"

	"URL_short/internal/service"
)

// URLHandler handles HTTP requests related to URL shortening and redirection.
type URLHandler struct {
	service *service.URLService
}

// NewURLHandler creates a new instance of URLHandler.
func NewURLHandler(service *service.URLService) *URLHandler {
	return &URLHandler{service: service}
}

// shortenRequest represents the expected JSON payload for creating a short URL.
type shortenRequest struct {
	URL string `json:"url"`
}

// CreateShortURL handles the creation of a short URL from a long URL.
func (h *URLHandler) CreateShortURL(w http.ResponseWriter, r *http.Request) {
	var req shortenRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	url, err := h.service.CreateShortURL(req.URL)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(url)
}

// RedirectURL handles the redirection from a short URL to the original long URL.
func (h *URLHandler) RedirectURL(w http.ResponseWriter, r *http.Request) {
	code := chi.URLParam(r, "code")

	longURL, err := h.service.GetOriginalURL(code)

	if err != nil {
		http.NotFound(w, r)
		return
	}

	http.Redirect(w, r, longURL, http.StatusFound)
}

// GetStats handles the retrieval of statistics for a given short code.
func (h *URLHandler) GetStats(w http.ResponseWriter, r *http.Request) {
	code := chi.URLParam(r, "code")

	stats, err := h.service.GetStats(code)

	if err != nil {
		http.NotFound(w, r)
		return
	}

	json.NewEncoder(w).Encode(stats)
}
