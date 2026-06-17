package service

import (
	"crypto/rand"
	"math/big"

	"URL_short/internal/models"
	"URL_short/internal/repository"
)
// URLService provides methods to manage URL shortening and retrieval.	
type URLService struct {
	repo *repository.URLRepository
}

// NewURLService creates a new instance of URLService.
func NewURLService(repo *repository.URLRepository) *URLService {
	return &URLService{repo: repo}
}

const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

func generateCode(length int) string {
	b := make([]byte, length)

	for i := range b {
		n, _ := rand.Int(rand.Reader, big.NewInt(int64(len(charset))))
		b[i] = charset[n.Int64()]
	}

	return string(b)
}

// CreateShortURL generates a short code for the given long URL and stores it in the database.
func (s *URLService) CreateShortURL(longURL string) (*models.URL, error) {
	url := &models.URL{
		LongURL:   longURL,
		ShortCode: generateCode(6),
		Clicks:    0,
	}

	err := s.repo.Create(url)

	if err != nil {
		return nil, err
	}

	return url, nil
}

// GetOriginalURL retrieves the original URL for a given short code.
func (s *URLService) GetOriginalURL(code string) (string, error) {
	url, err := s.repo.GetByShortCode(code)

	if err != nil {
		return "", err
	}

	_ = s.repo.IncrementClicks(code)

	return url.LongURL, nil
}

// GetStats retrieves statistics for a given short code.
func (s *URLService) GetStats(code string) (*models.URL, error) {
	return s.repo.GetByShortCode(code)
}
