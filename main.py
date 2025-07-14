from fastapi import FastAPI 
from typing import Optional 
from pydantic import BaseModel
from starlette.routing import Host


app=FastAPI()

@app.get('/blog')
def index(limit = 20,published: bool = True,sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs '}
    
@app.get('/blog/unpublish')
def index():
    return {"id": "content is shown"}


@app.get('/blog/{id}')
def index(id: int):
    return {"id": id}

@app.get('/blog/{id}/comments')
def index(id,limit=84): 
    return {'data':id,'limit':limit}

class Blog(BaseModel):
    title : str 
    body : str 
    published : Optional[bool]

@app.post('/blog')
def index(blog: Blog):
    return {'data': "Data is posted",'post':blog.title}

# if __name__== "__main__":
#     uvicorn.run(app, host="127.0.0.1",port=9000)
