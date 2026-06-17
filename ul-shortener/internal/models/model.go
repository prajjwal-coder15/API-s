package models

// URL represents a shortened URL with its associated data.
type URL struct {
	ID        int64  `json:"id"`
	ShortCode string `json:"short_code"`
	LongURL   string `json:"long_url"`
	Clicks    int64  `json:"clicks"`
}
