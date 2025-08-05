from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

# Logging setup
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    comment: str

@app.post("/chat")
async def chat(req: PromptRequest, authorization: str = Header(None)):
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")

    response = {
        "data": {
            "output": f"Thank you for your query. Here is the answer to: {req.prompt}",
            "score": 1.0
        }
    }

    logging.info(f"Prompt received: {req.prompt} | Comment: {req.comment}")
    return JSONResponse(content=response)
