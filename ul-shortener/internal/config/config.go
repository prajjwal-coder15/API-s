package config

import (
	"fmt"
	"os"
)

// Config holds the application configuration values.
type Config struct {
	Port string
	DBUrl string
	Environment string
}

// Load loads the application configuration from environment variables.
func Load() (*Config, error) {
	cfg := &Config{
		Port: os.Getenv("PORT"),
		Environment: os.Getenv("APP_ENV"),
	}

	cfg.DBUrl = fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_NAME"),
		os.Getenv("DB_SSLMODE"),
	)

	return cfg, nil
}
