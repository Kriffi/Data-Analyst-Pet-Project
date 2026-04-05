# Simple TODO API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)
![Uvicorn](https://img.shields.io/badge/uvicorn-0.34.0-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A lightweight **RESTful API** for managing a TODO list, built with **FastAPI** and **Python**.  
Data is stored in-memory (resets on server restart) — perfect for learning, prototyping, or as a foundation for a real database integration.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Example Requests & Responses](#example-requests--responses)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- ✅ Create, Read, Update, Delete tasks (full CRUD)
- ✅ Automatic interactive API documentation (Swagger UI & ReDoc)
- ✅ Data validation using Pydantic models
- ✅ UUID-based task identifiers
- ✅ In-memory storage (no database required for quick start)
- ✅ Ready for production extensions (auth, persistent DB, Docker)

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Programming language |
| **FastAPI** | Web framework (high performance, async support) |
| **Uvicorn** | ASGI server for running FastAPI |
| **Pydantic** | Data validation and serialization |

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher ([Download](https://www.python.org/downloads/))
- `pip` (usually comes with Python)
- Git (optional, for cloning the repository)

### Steps

1. **Clone the repository** (or download the source code)

    git clone https://github.com/yourusername/fastapi-todo-api.git
    cd fastapi-todo-api

2. **Create a virtual environment** (recommended)

    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies**

    pip install -r requirements.txt

    (The `requirements.txt` file contains `fastapi` and `uvicorn[standard]`)

---

## Running the Server

Start the server with auto-reload (useful for development):

    uvicorn main:app --reload

You should see:

    INFO:     Uvicorn running on http://127.0.0.1:8000
    INFO:     Application startup complete.

Open your browser at:

- Swagger UI (interactive docs): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc (alternative docs): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- Root endpoint: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — returns a welcome message.

To stop the server, press `Ctrl+C` in the terminal.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a single task by its UUID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Fully update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Task Object Schema

    {
      "id": "fa2706aa-f1f0-41db-a07e-870506ff6c02",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false
    }

- `id`: UUID (auto-generated, read-only)
- `title`: string (required)
- `description`: string or null (optional)
- `completed`: boolean (default: false)

---

## Example Requests & Responses

### 1. Create a Task

**Request:**

    curl -X POST "http://127.0.0.1:8000/tasks" \
      -H "Content-Type: application/json" \
      -d '{"title":"Write documentation","description":"Update README","completed":false}'

**Response (201 Created):**

    {
      "id": "fa2706aa-f1f0-41db-a07e-870506ff6c02",
      "title": "Write documentation",
      "description": "Update README",
      "completed": false
    }

### 2. Get All Tasks

**Request:**

    curl -X GET "http://127.0.0.1:8000/tasks"

**Response (200 OK):**

    [
      {
        "id": "fa2706aa-f1f0-41db-a07e-870506ff6c02",
        "title": "Write documentation",
        "description": "Update README",
        "completed": false
      }
    ]

### 3. Get a Single Task

**Request:**

    curl -X GET "http://127.0.0.1:8000/tasks/fa2706aa-f1f0-41db-a07e-870506ff6c02"

**Response (200 OK):**

    {
      "id": "fa2706aa-f1f0-41db-a07e-870506ff6c02",
      "title": "Write documentation",
      "description": "Update README",
      "completed": false
    }

If the task does not exist:

    {
      "detail": "Task not found"
    }

### 4. Update a Task (Full Update)

**Request:**

    curl -X PUT "http://127.0.0.1:8000/tasks/fa2706aa-f1f0-41db-a07e-870506ff6c02" \
      -H "Content-Type: application/json" \
      -d '{"title":"Write documentation","description":"Updated README and added examples","completed":true}'

**Response (200 OK):**

    {
      "id": "fa2706aa-f1f0-41db-a07e-870506ff6c02",
      "title": "Write documentation",
      "description": "Updated README and added examples",
      "completed": true
    }

### 5. Delete a Task

**Request:**

    curl -X DELETE "http://127.0.0.1:8000/tasks/fa2706aa-f1f0-41db-a07e-870506ff6c02"

**Response:** `204 No Content` (empty body)

---

## Screenshots

- Main 
<img width="1301" height="1318" alt="image" src="https://github.com/user-attachments/assets/8aff9e1a-3047-4688-be21-d16d7616d152" />



- POST Request Example  
  <img width="1201" height="1349" alt="image" src="https://github.com/user-attachments/assets/b50cc120-85d1-4825-a8b8-e2a308045b0b" />


-  GET /id Response  
  <img width="1187" height="1356" alt="image" src="https://github.com/user-attachments/assets/5b1fa75e-92f2-48ba-84d5-675a0cd9f544" />


- GET /all Response  
  <img width="1177" height="1349" alt="image" src="https://github.com/user-attachments/assets/5e0993a7-9238-4243-bd6d-4d2b151f2221" />


- PUT  
  <img width="1167" height="1348" alt="image" src="https://github.com/user-attachments/assets/9b6c3c3a-2a51-4e75-ab38-655c9af468d4" />


  - DELETE  
  <img width="1234" height="1351" alt="image" src="https://github.com/user-attachments/assets/3f578486-1c8e-4e00-b49b-8a4b9cb929f4" />

  


---

## Future Improvements

- Persistent database (SQLite / PostgreSQL with SQLAlchemy)
- JWT authentication and user-specific tasks
- Pagination and filtering for `GET /tasks`
- Dockerfile and docker-compose for easy deployment
- Unit tests with `pytest` and `httpx`
- Environment variables for configuration (using `python-dotenv`)

---

## License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## Author

Egor Podstreshnev – [GitHub](https://github.com/Kriffi)

Built with [FastAPI](https://fastapi.tiangolo.com/) – high performance, easy to learn, fast to code, ready for production.
