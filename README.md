# Containerized API Gateway with Health Checks & Active/Passive Failover
A  microservices architecture demonstrating reverse proxy routing, active-passive failover, containerized health probing, and chaos engineering simulations using Nginx, FastAPI, Django and Docker Compose.

## API Endpoints

| Method | Endpoint               | Internal Route         | Description                                                                 |
|--------|------------------------|------------------------|-----------------------------------------------------------------------------|
| GET    | /api/users/me          | /api/users/me          | Returns user payload and container metadata (server_id, hostname, timestamp). |
| GET    | /api/users/health      | /api/users/health      | Service health check endpoint (200 UP or 503 DOWN).                         |
| POST   | /api/users/simulate-crash | /api/users/simulate-crash | Toggles internal state to force HTTP 503 responses.                         |
| POST   | /api/users/restore     | /api/users/restore     | Resets internal state to healthy (200 OK).                                  |
| GET    | /api/inventory/health     | /api/inventory/health  | Inventory service health check endpoint.
