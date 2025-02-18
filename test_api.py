from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class Level(BaseModel):
    collisions: str
    backgroundImage: str
    doorPositionX: int
    doorPositionY: int
    playerStartPositionX: int
    playerStartPositionY: int

url = "http://localhost:8080/level/add"

@app.post("/level/add", response_model=Level)
async def add_level(level: Level):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=level.dict())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to add level")
    return level
