def blog_serializer(blog) -> dict:
     return{
         "id": str(blog["_id"]),
         "author": blog["author"],
         "title": blog["title"],
         "content": blog["content"]
     }

def comment_serializer(comment) -> dict:
    return{
        "id": str(comment["_id"]),
        "content": comment["content"]
    }

def blogs_serializer(blogs) -> list:
    return [blog_serializer(blog) for blog in blogs]

def comments_serializer(comments) -> list:
    return [comment_serializer(comment) for comment in comments]