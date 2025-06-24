from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

post_dir = "posts"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://vuefastapiblog.netlify.app",
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


@app.get("/posts/{post_name}")
async def read_post(post_name: str):
    file_path = os.path.join(post_dir, f"{post_name}.md")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Post not found.")
    with open(file_path, "r") as p:
        content = p.read()
    return {"content": content}
