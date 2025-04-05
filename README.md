# BE Capstone Project: Task Management API

Task Management API using Django and Django REST Framework.

The API will allow users to manage their tasks by creating, updating, deleting, and marking tasks as complete or incomplete .

## Register - Login and Logout - Endpoints

### Register

**URL:** `POST /api/register/`  
**Content-Type:** `application/json`

##### Request Body

```json
{
  "username": "username",
  "email": "email@example.com",
  "password": "1234567890"
}
```

##### Success Response

```json
{
  "id": 1,
  "username": "username",
  "email": "email@example.com",
  "token": "d23f7f8628486d12215b09a5658d23d1d4c766ed",
}
```

#### LOGIN

**Endpoint:** `POST /api/login/`  
**Content-Type:** `application/json`

### Body

```json
{
  "username": "username",
  "password": "1234567890"
} 
```

#### Response

```json
{
  "token": "8e2b6194a363d1c8135e5874a9b9dd31d91310a2",
  "user": {
    "id": 5,
    "username": "username",
    "password": "pbkdf2_sha256$870000$LWah2qztMPpqlriPOTYwWH$RnC2nnTbuPazJ5isufxhI6PiRcnrzG22Rj+Iuc8S+X4=",
    "email": "email187@gmail.com"
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

## Task CRUD

### Create

**URL:** `POST /api/tasks/create`  
**Content-Type:** `application/json`
**Authorization :** Token <your_token>

### Body

```json
{
  "title": "This field is required.",
  "description": "This field is required.",
  "due_date": "2025-11-11",
  "priority": "High",
  "status": "Completed",
  "user": 3
} 
```

#### Response

```json
{
    "id": 6,
    "title": "This field is required.",
    "description": "This field is required.",
    "due_date": "2025-11-11",
    "priority": "High",
    "status": "Completed",
    "created_at": "2025-04-05T15:40:03.720260Z",
    "user": 3
}

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
