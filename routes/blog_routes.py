from fastapi import APIRouter
from config.database import collections_post
from models.blog_models import Blog
from schemas.blog_schemas import blog_serializer,blogs_serializer,comment_serializer,comments_serializer
from bson import ObjectId, objectid


blog_api_router = APIRouter()

@blog_api_router.get("/")
async def get_blog_post():
    blog = blogs_serializer(collections_post.find())
    return {"status": "ok", "data":blog}


@blog_api_router.get("/{id}")
async def get_post(id: str):
    blog = blogs_serializer(collections_post.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": blog}

@blog_api_router.post("/")
async def post_blog(blog: Blog):
    _id = collections_post.insert_one(dict(blog))
    blog = blogs_serializer(collections_post.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": blog}


@blog_api_router.put("/{id}")
async def update_post(id: str, blog: Blog):
    collections_post.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(blog)
    })
    blog = blogs_serializer(collections_post.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": blog}

@blog_api_router.delete("/{id}")
async def update_post(id: str):
    collections_post.find_one_and_delete({"_id": ObjectId(id)}, {
    })
    return {"status": "ok", "data": []}

@blog_api_router.post("/comment")
async def comment_on_post(comment: Comment):
    _id = collections_post.insert_one(dict(comment))
    comment = comments_serializer(collections_post.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": comment}