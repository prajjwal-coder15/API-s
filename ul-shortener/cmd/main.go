package main

import (
	"database/sql"
	"log"
	"log/slog"
	"net/http"

	"github.com/joho/godotenv"
	"github.com/go-chi/chi/v5"
	_ "github.com/lib/pq"

	"URL_short/internal/logger"
	"URL_short/internal/config"
	"URL_short/internal/handlers"
	"URL_short/internal/repository"
	"URL_short/internal/service"
)

func main() {
		logger := logger.New()
		godotenv.Load()

		cfg, err := config.Load()
		if err != nil {
			logger.Error("failed to load configuration", slog.Any("error", err))
			log.Fatal(err)
		}

	connStr := cfg.DBUrl
	db, err := sql.Open("postgres", connStr)

	if err != nil {
		logger.Error("failed to connect to database", slog.Any("error", err))
		log.Fatal(err)
	}

	repo := repository.NewURLRepository(db)
	svc := service.NewURLService(repo)
	handler := handlers.NewURLHandler(svc)

	r := chi.NewRouter()

	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
	    w.Write([]byte("URL Shortener API Running"))
    	})
	r.Post("/api/shorten", handler.CreateShortURL)
	r.Get("/{code}", handler.RedirectURL)
	r.Get("/api/stats/{code}", handler.GetStats)

	log.Println("server running on :8080")

	http.ListenAndServe(":8080", r)
}
