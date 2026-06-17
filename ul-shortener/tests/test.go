package tests

import (
	"testing"

	"URL_short/internal/models"
)

func TestURLModel(t *testing.T) {
	url := models.URL{
		LongURL: "https://google.com",
	}

	if url.LongURL == "" {
		t.Error("expected long url")
	}
}
