# 🔐 Sample Flask Auth

## 📝 About the project

Authentication API built with **Flask** and **Flask-Login**, using a **MySQL** database containerized with **Docker** to persist user data. The project implements a complete authentication system with registration, login, logout and session management.

Repository created to store the code of the authentication API with a database, demonstrating essential concepts such as:
- A complete authentication system
- Session management with Flask-Login
- Data persistence with SQLAlchemy and MySQL
- Containerization with Docker
- Password hashing
- ORM (Object-Relational Mapping)

## 🚀 Technologies used

- **Python 3.x**
- **Flask 2.3.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - Database ORM
- **Flask-Login 0.6.2** - Authentication and session management
- **MySQL** - Relational database
- **Docker** - Database containerization
- **PyMySQL 1.1.0** - MySQL connector for Python
- **Werkzeug 2.3.0** - WSGI toolkit and password hashing
- **Cryptography 41.0.7** - Cryptography library

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- Docker and Docker Compose installed
- pip (Python package manager)

### Database Setup with Docker

1. Start the MySQL container using Docker Compose:
```bash
docker-compose up -d
```

2. Check that the container is running:
```bash
docker ps
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/sample-flask-auth.git
cd sample-flask-auth
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

### Running the application
```bash
python app.py
```

The API will be available at: `http://localhost:5000`

### Stopping the services
```bash
# Stop the MySQL container
docker-compose down

# Stop and remove volumes (deletes the data)
docker-compose down -v
```

## 🐳 Docker Configuration

### MySQL credentials (docker-compose.yml)
```yaml
MYSQL_USER: admin
MYSQL_PASSWORD: admin123
MYSQL_DATABASE: flask-crud
MYSQL_ROOT_PASSWORD: admin123
```

### Application connection
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin123@localhost:3306/flask-crud'
```

## 🎯 Features

- 📝 **User registration** with data validation
- 🔑 **Login** with secure authentication
- 🚪 **Logout** to end the session
- 🔒 **Protected routes** that require authentication
- 👤 **Session management** with Flask-Login
- 💾 **Data persistence** in MySQL via Docker
- 🔐 **Password hashing** with Werkzeug
- 🐳 **Containerized database**

## 🛠️ Data model

### User

| Field | Type | Description |
|-------|------|-----------|
| id | Integer | Primary key (auto-increment) |
| username | String | Username (unique) |
| email | String | User email (unique) |
| password | String | Hashed password |
| created_at | DateTime | Account creation date |

## 📸 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth required |
|--------|----------|-----------|--------------|
| POST | `/register` | Registers a new user | No |
| POST | `/login` | Authenticates the user and creates a session | No |
| POST | `/logout` | Ends the user's session | Yes |
| GET | `/profile` | Returns the logged-in user's data | Yes |

## 💡 Usage examples

### Register a new user
```bash
POST /register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Usuário registrado com sucesso",
  "user_id": 1
}
```

### Log in
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Login realizado com sucesso",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  }
}
```

### Access the profile (protected route)
```bash
GET /profile
Cookie: session=...
```

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00"
}
```

### Log out
```bash
POST /logout
Cookie: session=...
```

**Response:**
```json
{
  "message": "Logout realizado com sucesso"
}
```

## 🔒 Security Features

- **Werkzeug Security**: Salted password hashing
- **Flask-Login**: Secure session management
- **SQLAlchemy**: Protection against SQL Injection
- **Data validation**: User input checks
- **Encrypted sessions**: Secure cookies
- **Docker**: Database isolation

## 🗃️ Database Structure

The project uses **MySQL containerized with Docker**, ensuring:
- An isolated, reproducible environment
- Easy setup and deployment
- Data persistence in volumes
- Portability across environments
- Referential integrity
- ACID transactions

## 🐳 Useful Docker commands
```bash
# Start the containers
docker-compose up -d

# View MySQL logs
docker-compose logs db

# Access MySQL from the command line
docker exec -it  mysql -u admin -p

# Stop the containers
docker-compose down

# Restart the containers
docker-compose restart
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
