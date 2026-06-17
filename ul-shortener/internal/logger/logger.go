package logger

import (
	"log/slog"
	"os"
)

// New creates and returns a new slog.Logger instance configured to write JSON logs to standard output with a log level of Info.
func New() *slog.Logger {
	handler := slog.NewJSONHandler(
		os.Stdout,
		&slog.HandlerOptions{
			Level: slog.LevelInfo,
		},
	)

	return slog.New(handler)
}
