# 🔗 URL Shortener

A Bitly-like URL shortening service built with Go and PostgreSQL. This project focuses on building RESTful APIs, database integration, clean architecture, and testing best practices.

---

## 🎯 Goal

Create a URL shortening service that allows users to:

- Generate short URLs from long URLs
- Redirect users to the original URL
- Track click analytics
- Store and manage data in PostgreSQL

---

## ✨ Features

- 🔗 Create short URLs
- 🚀 Redirect short URLs to original links
- 📊 Track click counts
- 🗄️ PostgreSQL data storage
- 🧪 Unit testing support
- 🏗️ Clean architecture using Repository Pattern

---

## 🛠️ Tech Stack

- **Language:** Go
- **Router:** Gorilla Mux or Chi
- **Database:** PostgreSQL
- **Migrations:** golang-migrate
- **Testing:** Go Testing Package

---

## 📂 Project Structure

```text
url-shortener/
├── cmd/
├── internal/
│   ├── handlers/
│   ├── service/
│   ├── repository/
│   └── models/
├── migrations/
└── tests/
```

### Folder Responsibilities

| Folder | Purpose |
|----------|----------|
| `cmd/` | Application entry point |
| `handlers/` | HTTP request handlers |
| `service/` | Business logic |
| `repository/` | Database operations |
| `models/` | Data models and DTOs |
| `migrations/` | Database schema migrations |
| `tests/` | Unit and integration tests |

---

## 📡 API Endpoints

<img width="1262" height="145" alt="Screenshot 2026-06-16 185107" src="https://github.com/user-attachments/assets/28d0ce16-9114-4fa5-96c9-6482eac666de" />

### Create Short URL



```http
POST /api/shorten
```

#### Request

```json
{
  "url": "https://example.com/very-long-url"
}
```

#### Response

```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:8080/abc123"
}
```
<img width="1262" height="282" alt="Screenshot 2026-06-16 185052" src="https://github.com/user-attachments/assets/434b5123-e416-44a8-bea5-3ecec6ad782c" />

---

### Redirect to Original URL

```http
GET /:shortCode
```

#### Example

```http
GET /abc123
```

**Response:** Redirects to the original URL.
---
<img width="1631" height="490" alt="Screenshot 2026-06-17 131346" src="https://github.com/user-attachments/assets/3775987c-3daf-4e8f-9021-4a8ff820ac36" />

---

### Get URL Statistics

```http
GET /api/stats/:shortCode
```

#### Response

```json
{
  "short_code": "abc123",
  "original_url": "https://example.com/very-long-url",
  "clicks": 42
}
```
<img width="1398" height="292" alt="Screenshot 2026-06-17 131429" src="https://github.com/user-attachments/assets/374127c8-5028-4000-8a34-fbe1bfb2d977" />

---

## 🗄️ Database Schema

### URLs Table

| Column | Type |
|----------|----------|
| id | UUID / SERIAL |
| short_code | VARCHAR |
| original_url | TEXT |
| clicks | INTEGER |
| created_at | TIMESTAMP |

---

## 🧠 Concepts Covered

- REST API Design
- URL Encoding & Short Code Generation
- HTTP Redirects
- PostgreSQL Integration
- Database Migrations
- Repository Pattern
- Dependency Injection
- Error Handling
- Unit Testing

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### Install Dependencies

```bash
go mod tidy
```

### Configure Environment

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=url_shortener
```

### Run Migrations

```bash
migrate -path migrations -database <DATABASE_URL> up
```

### Start Server

```bash
go run ./cmd
```

---

## 🧪 Running Tests

```bash
go test ./...
```

---

## 🎓 Learning Outcomes

By completing this project, you will gain experience with:

- Building RESTful services in Go
- Structuring scalable applications
- Working with PostgreSQL
- Implementing repository patterns
- Writing maintainable and testable code
- Designing production-ready APIs

---

## 🚀 Future Improvements

- Custom short URLs
- URL expiration
- User authentication
- Analytics dashboard
- Rate limiting
- Redis caching
- Docker support
- QR code generation

---

## 📜 License

This project is intended for learning and portfolio purposes.
