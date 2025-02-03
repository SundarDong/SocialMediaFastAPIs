from fastapi import FastAPI

app = FastAPI()


@app.get("/") #This is the decorator, When you use in the ip of the / then it direct print the message
def read_root():
    return {"message": "Welcome to my API !!!"}

    #if the decorator doesnt have same get url then it will run the first line of code of function.

@app.get("/posts")
def get_posts():
    return {"data": "This is my first data"}