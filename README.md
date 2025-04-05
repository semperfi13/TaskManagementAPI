# BE Capstone Project: Task Management API

Task Management API using Django and Django REST Framework.

The API will allow users to manage their tasks by creating, updating, deleting, and marking tasks as complete or incomplete .

## API URL

### Can test it using [Postman](https://www.postman.com/)

**URL:** [semperfi.pythonanywhere.com](https://semperfi.pythonanywhere.com)

# Register - Login and Logout - Endpoints

### Register

**URL:** `POST /api/register/`  
**Content-Type:** `application/json`

##### Request Body

```json
{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "password": "strongpassword123"
}
```

##### Success Response

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john.doe@example.com",
  "token": "d23f7f8628486d12215b09a5658d23d1d4c766ed"
}
```

#### LOGIN

**Endpoint:** `POST /api/login/`  
**Content-Type:** `application/json`

### Body

```json
{
  "username": "john_doe",
  "password": "strongpassword123"
} 
```

#### Response

```json
{
  "token": "8e2b6194a363d1c8135e5874a9b9dd31d91310a2",
  "user": {
    "id": 5,
    "username": "john_doe",
    "password": "pbkdf2_sha256$870000$LWah2qztMPpqlriPOTYwWH$RnC2nnTbuPazJ5isufxhI6PiRcnrzG22Rj+Iuc8S+X4=",
    "email": "john.doe@example.com"
  }
}

```

#### LOGOUT

**Endpoint:** `POST /api/logout/`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

#### Response

```json
{
    "message": "Successfully logged out"
}

```

# Task CRUD

### Read

**URL:** `GET /api/tasks/`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

```json
[
  {
    "id": 3,
    "title": "Complete project report",
    "description": "Finish writing the final project report for the client",
    "due_date": "2025-11-11",
    "priority": "High",
    "status": "Pending",
    "created_at": "2025-04-05T15:38:14.381704Z",
    "user": 3
  },
  {
    "id": 4,
    "title": "Email client about project updates",
    "description": "Send an update email to the client regarding project progress",
    "due_date": "2025-11-11",
    "priority": "Medium",
    "status": "Pending",
    "created_at": "2025-04-05T15:38:15.037682Z",
    "user": 3
  },
  {
    "id": 6,
    "title": "Prepare for team meeting",
    "desjohn_doecription": "Prepare slides and agenda for the next team meeting",
    "due_date": "2025-11-11",
    "priority": "Low",
    "status": "Pending",
    "created_at": "2025-04-05T15:40:03.720260Z",
    "user": 3
  }
]
```

### Create

**URL:** `POST /api/tasks/create`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

### Body

```json
{
  "title": "Prepare the project proposal",
  "description": "Create the initial project proposal document",
  "due_date": "2025-05-01",
  "priority": "High",
  "status": "Pending",
  "user": 3
} 
```

#### Response

```json
{
    "id": 6,
    "title": "Prepare the project proposal",
    "description": "Create the initial project proposal document",
    "due_date": "2025-05-01",
    "priority": "High",
    "status": "Pending",
    "created_at": "2025-04-05T15:40:03.720260Z",
    "user": 3
}

```

### Details

**URL:** `GET /api/tasks/retrieve/<pk>/`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

#### Response

```json
{
  "id": 5,
  "title": "Complete the market research report",
  "description": "Finish writing and compiling the market research report for Q2",
  "due_date": "2025-04-12",
  "priority": "High",
  "status": "Pending",
  "created_at": "2025-04-05T15:38:15.683309Z",
  "user": 3
}

```

### Update

**URL:** `PUT /api/tasks/update/<pk>/`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

### Body

```json
{
  "title": "Complete market research report",
  "description": "Finalize the report based on client feedback",
  "due_date": "2025-04-15",
  "priority": "High",
  "status": "In Progress",
  "user": 3
}

```

#### Response

```json
{
  "title": "Complete market research report",
  "description": "Finalize the report based on client feedback",
  "due_date": "2025-04-15",
  "priority": "High",
  "status": "In Progress",
  "user": 3
}

```

### Delete

**URL:** `Delete /api/tasks/delete/<pk>/`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>


#### Response

```json
{
  "message": "Task has been delete Successfully"
}
```

### Update Task status

**URL:** `PATCH /api/task/update/<pk>/status`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>


#### Response

```json
{
  "id": 5,
  "title": "Complete market research report",
  "description": "Finalize the report based on client feedback",
  "due_date": "2025-04-15",
  "priority": "High",
  "status": "In Progress",
  "user": 3,
  "created_at": "2025-04-05T15:38:15.683309Z",
  "timestamp": "2025-04-05T22:05:27.675817Z",
}
```

### Filter Task

**URL:** `GET /api/tasks/?priority=<priority>&Status=<status>&due_date=<Y-m-d>`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>


#### Response

```json
[
  {
    "id": 5,
    "title": "Complete market research report",
    "description": "Finalize the report based on client feedback",
    "due_date": "2025-04-12",
    "priority": "Low",
    "status": "Pending",
    "created_at": "2025-04-05T15:38:15.683309Z",
    "timestamp": null,
    "user": 3
  }
]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
