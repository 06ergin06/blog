from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

post_dir = "posts"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/posts/")
async def list_posts():

    all_files = os.listdir(post_dir)
    post_titles = []
    for filename in all_files:
        if filename.endswith(".md"):
            post_name = os.path.splitext(filename)[0]
            post_titles.append(post_name)
    return {"posts": post_titles}
