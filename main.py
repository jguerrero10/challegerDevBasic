from typing import Dict

from fastapi import FastAPI

app = FastAPI()

app.title = "Challenger Dev Python Senior"
app.version = "0.0.1"


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Challenger Dev Python Senior"}
