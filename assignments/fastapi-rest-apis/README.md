# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage tasks. Practice defining API routes, validating request data, returning JSON responses, and handling HTTP errors.

## 📝 Tasks

### 🛠️	Read Tasks from the API

#### Description
Complete the starter code to create a FastAPI application that lets clients retrieve all tasks or retrieve one task by its ID.

#### Requirements
Completed program should:

- Define a `TaskCreate` Pydantic model with a required, non-empty `title` and an optional `completed` value that defaults to `false`.
- Implement `GET /tasks` to return all tasks as JSON.
- Implement `GET /tasks/{task_id}` to return the matching task, or HTTP 404 if the ID does not exist.


### 🛠️	Create and Test Tasks

#### Description
Add an endpoint that accepts a new task, assigns it a unique ID, and returns the created task. Run the API and test its endpoints through FastAPI's interactive documentation.

From this assignment folder, install the dependencies and start the server:

```bash
python -m pip install fastapi uvicorn
uvicorn starter_code:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the API.

#### Requirements
Completed program should:

- Implement `POST /tasks` to accept a valid task and store it in memory.
- Assign each created task a unique integer ID and return the created task with HTTP 201.
- Reject a task with a missing or empty title using request validation.
- Demonstrate successful GET and POST requests and a 404 response for an unknown task ID in the interactive documentation.
