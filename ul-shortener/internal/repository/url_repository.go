package repository

import (
	"database/sql"

	"URL_short/internal/models"
)

// URLRepository provides methods to interact with the URLs in the database.
type URLRepository struct {
	DB *sql.DB
}

// NewURLRepository creates a new instance of URLRepository.
func NewURLRepository(db *sql.DB) *URLRepository {
	return &URLRepository{DB: db}
}

// Create inserts a new URL into the database.
func (r *URLRepository) Create(url *models.URL) error {
	query := `
	INSERT INTO urls(short_code, long_url, clicks)
	VALUES($1,$2,$3)
	RETURNING id`

	return r.DB.QueryRow(
		query,
		url.ShortCode,
		url.LongURL,
		url.Clicks,
	).Scan(&url.ID)
}

// GetByShortCode retrieves a URL by its short code.
func (r *URLRepository) GetByShortCode(code string) (*models.URL, error) {
	var url models.URL

	query := `
	SELECT id, short_code, long_url, clicks
	FROM urls
	WHERE short_code=$1`

	err := r.DB.QueryRow(query, code).Scan(
		&url.ID,
		&url.ShortCode,
		&url.LongURL,
		&url.Clicks,
	)

	if err != nil {
		return nil, err
	}

	return &url, nil
}

// IncrementClicks increments the click count for a URL by its short code.
func (r *URLRepository) IncrementClicks(code string) error {
	_, err := r.DB.Exec(
		"UPDATE urls SET clicks = clicks + 1 WHERE short_code=$1",
		code,
	)

	return err
}
