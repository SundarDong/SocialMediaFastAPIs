from random import randrange
from typing import Optional
from fastapi import Body, FastAPI
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

@app.get("/") #This is the decorator, When you use in the ip of the / then it direct print the message
def read_root():
    return {"message": "Welcome to my API !!!"}

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
    
    #Learning the POST metho of HTTP
#Post method ma data post garne milxa API ma

#title str, content str, category