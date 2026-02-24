# 📝 Task Manager API

A RESTful Task Manager API built with **Flask**, **MongoDB**, and **JWT Authentication**.

This project demonstrates secure user authentication, protected routes, and user-based task management using a clean project structure.

---

## 🚀 Features

- 🔐 User Registration (Password Hashing with Bcrypt)
- 🔑 JWT Authentication (Login System)
- 🛡 Protected Routes
- 📝 Create Tasks
- 📋 View User-Specific Tasks
- ✏️ Update Tasks
- 🗑 Delete Tasks
- 🧱 Clean MVC-style Project Structure
- 🌱 Environment Variable Configuration

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **MongoDB**
- **Flask-PyMongo**
- **Flask-JWT-Extended**
- **Flask-Bcrypt**
- **Python-Dotenv**

---

## 📂 Project Structure

```

flask_mongo_api/
│
├── app.py
├── config.py
├── extensions.py
├── .env
│
├── models/
│   ├── **init**.py
│   ├── user_model.py
│   └── task_model.py
│
├── routes/
│   ├── **init**.py
│   ├── auth_routes.py
│   └── task_routes.py

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask flask-pymongo flask-jwt-extended flask-bcrypt python-dotenv
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
MONGO_URI=mongodb://localhost:27017/taskdb
JWT_SECRET_KEY=your_super_secret_key
```

To generate a secure key:

```python
import secrets
print(secrets.token_hex(32))
```
<img width="1036" height="257" alt="Screenshot 2026-02-24 170604" src="https://github.com/user-attachments/assets/738fc645-a435-4454-a51a-331692275e2f" />

---

### 5️⃣ Run the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 📌 API Endpoints

### 🔐 Authentication

### Welcome page
<img width="706" height="538" alt="Screenshot 2026-02-24 162931" src="https://github.com/user-attachments/assets/dbe1a1d7-4a8d-477e-bc09-9e9732feea07" />


#### Register User

```
POST /register
```

Body:

```json
{
  "username": "john",
  "password": "1234"
}
```
<img width="972" height="745" alt="Screenshot 2026-02-24 163056" src="https://github.com/user-attachments/assets/c74e3cd3-b47d-476b-8f09-d52c09f0da64" />

#### Login User

```
POST /auth/login
```

Body:

```json
{
  "username": "john",
  "password": "1234"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN"
}
```
<img width="1594" height="835" alt="Screenshot 2026-02-24 163240" src="https://github.com/user-attachments/assets/827e46ef-0e3d-4584-91fd-150fac80b0b5" />

---

### 📝 Tasks (Protected Routes)

All task routes require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

#### Create Task

```
POST /tasks/
```

Body:

```json
{
  "title": "Learn Flask JWT"
}
```
<img width="1599" height="630" alt="Screenshot 2026-02-24 164516" src="https://github.com/user-attachments/assets/1c59824f-2891-4fcc-b583-0540fc9fe68a" />
<img width="1610" height="642" alt="Screenshot 2026-02-24 164530" src="https://github.com/user-attachments/assets/c6fb99b3-785e-45cb-9ab1-3653362ed81b" />

---

#### Get All User Tasks

```
GET /tasks/
```
<img width="1600" height="881" alt="Screenshot 2026-02-24 164648" src="https://github.com/user-attachments/assets/a479b46c-a4bd-4121-91bb-c29fd48c24bc" />

---

#### Update Task

```
PUT /tasks/<task_id>
```

Body:

```json
{
  "title": "Updated Title",
  "completed": true
}
```
### update later
---

#### Delete Task

```
DELETE /tasks/<task_id>
```
### Update Later
---

## 🔐 Authentication Flow

1. Register a new user
2. Login to receive JWT token
3. Include token in Authorization header:

   ```
   Authorization: Bearer <token>
   ```
4. Access protected task routes

---

## 🧠 What This Project Demonstrates

* Secure password hashing
* Token-based authentication
* User-specific data isolation
* REST API design principles
* Clean Flask project architecture
* MongoDB integration

---

## 🚀 Future Improvements

* Refresh Tokens
* Role-Based Access Control (Admin/User)
* Input Validation (Marshmallow)
* Pagination
* Docker Deployment
* Production WSGI setup (Gunicorn)

---

## 👨‍💻 Author

<h2>PRAJJWAL KUMAR</h2><h3>CSE Engineer</h3>

---

## 📄 License

This project is open-source and available under the MIT License.

```
