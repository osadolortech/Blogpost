from routes.blog_routes import blog_api_router
from fastapi import FastAPI 

app = FastAPI()

app.include_router(blog_api_router)