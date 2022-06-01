def blog_serializer(blog) -> dict:
     return{
         "id": str(blog["_id"]),
         "author": blog["author"],
         "content": blog["content"]
     }

def blogs_serializer(blogs) -> list:
    return [blog_serializer(blog) for blog in blogs]