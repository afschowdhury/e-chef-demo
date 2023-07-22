import uvicorn
import os
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import utils.e_chef_answer as e_chef_answer
from fastapi.middleware.cors import CORSMiddleware

PORT = 8080
if os.getenv("PORT"):
    PORT = int(os.getenv("PORT"))

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/start_analysis")
async def read_root(request: Request):
    csv_path = os.path.abspath("data/restaurant_sales_dataset.csv")
    chat_chef_response = e_chef_answer.get_initial_analysis(csv_path)

    response = {
        "chat_chef_response": chat_chef_response
    }
    return JSONResponse(
        content=response, status_code=200
    )


@app.post("/ask_e_chef")
async def read_root(request: Request):
    upcoming_stream = await request.json()
    user_message = upcoming_stream["user"]
    chat_chef_response = e_chef_answer.get_chat_chef_response(user_message)

    response = {
        "user_message": user_message,
        "chat_chef_response": chat_chef_response
    }
    return JSONResponse(
        content=response, status_code=200
    )


if __name__ == "__main__":
    # run the server on port 8080
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=False)
