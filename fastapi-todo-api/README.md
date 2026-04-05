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
   ```bash
   git clone https://github.com/yourusername/fastapi-todo-api.git
   cd fastapi-todo-api
