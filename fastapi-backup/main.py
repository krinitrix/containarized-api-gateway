import os
import socket
from datetime import datetime, timezone
from fastapi import FastAPI, Response, status

app = FastAPI(title="User Service - Primary", docs_url="/docs")

# Global state to control simulated health for chaos engineering
IS_HEALTHY = True
SERVER_ID = os.getenv("SERVER_ID", "fastapi-primary")
SERVICE_NAME = "user-service"


@app.get("/api/users/me")
def get_user_profile():
    """
    Main user domain endpoint. Fails with HTTP 503 if the server is in a crashed state,
    allowing Nginx to automatically failover to the backup instance.
    """
    if not IS_HEALTHY:
        return Response(
            content='{"error": "Service Unavailable (Simulated Failure)"}',
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            media_type="application/json"
        )
    
    return {
        "data": {
            "user_id": 101,
            "username": "devops_candidate",
            "role": "admin"
        },
        "meta": {
            "service": SERVICE_NAME,
            "server_id": SERVER_ID,
            "container_hostname": socket.gethostname(),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }


@app.get("/health")
def health_check():
    """
    Queried by Docker and Nginx health checks.
    Returns HTTP 200 OK when healthy, or HTTP 503 Service Unavailable when crashed.
    """
    if not IS_HEALTHY:
        return Response(
            content=f'{{"status": "DOWN", "server_id": "{SERVER_ID}"}}',
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            media_type="application/json"
        )
    
    return {
        "status": "UP",
        "service": SERVICE_NAME,
        "server_id": SERVER_ID,
        "container_hostname": socket.gethostname()
    }


@app.post("/simulate-crash")
def simulate_crash():
    """
    Chaos Endpoint: Sets IS_HEALTHY to False to force /health and domain routes to return HTTP 503.
    """
    global IS_HEALTHY
    IS_HEALTHY = False
    return {
        "message": f"{SERVER_ID} crash state activated. Health check will now return HTTP 503.",
        "server_id": SERVER_ID,
        "is_healthy": IS_HEALTHY
    }


@app.post("/restore")
def restore_server():
    """
    Resets the server back to a healthy state.
    """
    global IS_HEALTHY
    IS_HEALTHY = True
    return {
        "message": f"{SERVER_ID} restored to healthy state.",
        "server_id": SERVER_ID,
        "is_healthy": IS_HEALTHY
    }