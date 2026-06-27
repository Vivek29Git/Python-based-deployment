import os
import logging
from fastapi import FastAPI
from pydantic import BaseModel

# Configure structured logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("python-app")

app = FastAPI(title="CI-CD Python App", version="1.0.0")

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"status": "success", "message": "Hello from AWS ECS!"}

@app.get("/health")
async def health_check():
    """Endpoint for AWS ECS target group health checks."""
    logger.info("Health check pinged")
    return {"status": "healthy"}

@app.post("/echo")
async def echo_message(payload: Msg):
    logger.info(f"Echoing back message: {payload.msg}")
    return {"received": payload.msg}

if __name__ == "__main__":
    import uvicorn
    # Read port from environment variable, default to 8080 for ECS
    port = int(os.getenv("PORT", 8080))
    
if __name__ == "__main__":
    import uvicorn
    # Read port from environment variable, default to 8080 for ECS
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
