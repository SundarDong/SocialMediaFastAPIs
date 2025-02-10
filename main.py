from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool= True
    rating : Optional[int] = None

my_posts = [{"title":"First post title", "content":"First post content", "id":1},
                {"title":"Second post title", "content":"Second post content", "id":2}
                ]
def find_posts(id):
    for p in my_posts:
        if p["id"]== id:
            return p


@app.get("/") #This is the decorator, When you use in the ip of the / then it direct print the message
def read_root():
    return {"message": "Welcome to my API !!!"}
int
    #if the decorator doesnt have same get url then it will run the first line of code of function.

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/post")
def create_posts(post: Post): #Yo line ma Body ma vako sabai content lai extract garera paython dictornary ma banauca rew payLoad(variable) ma set garxa rakhxa
    post_dict=post.dict()
    post_dict['id']= randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}



@app.get("/posts/latest")
def get_latest_post():
    post= my_posts[len(my_posts)-1]
    return {"details": post}

@app.get("/post/{id}")
def get_post(id : int, response: Response):
    post = find_posts(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    print(post)
    return {"post_details": post}