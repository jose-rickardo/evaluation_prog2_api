from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

# Q1
@app.get("/ping")
async def ping():
    return PlainTextResponse("pong", status_code=200)

# Q2
@app.get("/home", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome home!</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# Q3
@app.exception_handler(404)
async def not_found(request: Request, exc):
    html_404 = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>404 NOT FOUND</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_404, status_code=404)

# Q4
class posts(BaseModel):
    autor: str
    title:str
    creation_datetime: datetime

stocage_en_memoire_vive: List[posts] = []

@app.post("/posts", liste = List[posts] , status_code=404)
async def le_posts(posts: List[posts]):
    stocage_en_memoire_vive.extend(posts)
    return stocage_en_memoire_vive

# Q5
@app.get("/posts")
async def post():
    return JSONResponse(content=posts, status_code=200)

# Q6
@app.put("/posts")
async def post(post: Post):
    for i, existing in enumerate(posts):
        if existing["title"] == post.title:
            if existing["content"] != post.content:
                posts[i]["content"] = post.content
                return JSONResponse({"message": "mis à jour avec succée"}, status_code=200)
            else:
                return JSONResponse({"message": "Aucun changement"}, status_code=200)
    posts.append(post.dict())
    return JSONResponse({"message": "ajouté avec succée"}, status_code=201)


