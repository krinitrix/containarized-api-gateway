# Containerized API Gateway with Health Checks & Active/Passive Failover
A  microservices architecture demonstrating reverse proxy routing, active-passive failover, containerized health probing, and chaos engineering simulations using Nginx, FastAPI, Django and Docker Compose.
<img width="800" height="600" alt="Containarized_api_gateway" src="https://github.com/user-attachments/assets/fadd23f3-b142-4329-97b3-5257f5012979" />

## API Endpoints

| Method | Endpoint               | Internal Route         | Description                                                                 |
|--------|------------------------|------------------------|-----------------------------------------------------------------------------|
| GET    | /api/users/me          | /api/users/me          | Returns user payload and container metadata (server_id, hostname, timestamp). |
| GET    | /api/users/health      | /api/users/health      | Service health check endpoint (200 UP or 503 DOWN).                         |
| POST   | /api/users/simulate-crash | /api/users/simulate-crash | Toggles internal state to force HTTP 503 responses.                         |
| POST   | /api/users/restore     | /api/users/restore     | Resets internal state to healthy (200 OK).                                  |
| GET    | /api/inventory/health     | /api/inventory/health  | Inventory service health check endpoint.


## System Components

| Component        | Technology             | Role                                                                 |
|------------------|------------------------|----------------------------------------------------------------------|
| API Gateway      | Nginx                  | Reverse proxy, path-based routing, load balancing, active-passive failover |
| User Service     | FastAPI (Uvicorn)      | High-performance microservice with built-in chaos endpoints          |
| Inventory Service| Django (Gunicorn/WSGI) | Relational CRUD microservice connected to PostgreSQL                 |
| Containerization | Docker & Docker Compose| Multi-container orchestration, isolated bridge networking, health monitoring |
