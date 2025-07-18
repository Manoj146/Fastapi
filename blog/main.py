from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog,user,authentication

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)

app.include_router(blog.router)

app.include_router(user.router)











# def get_db():
#     db=Sessionlocal()
#     try:
#         yield db 
#     finally:
#         db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
# def create(request: schemas.Blog,db: Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['Blogs'])
# def all(db: Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs 

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
# def index(id,response: Response,db: Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#         # response.status_code= status.HTTP_404_NOT_FOUND
#         # return {'details': f"Blog with id {id} not found"}
#     return blogs 


# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def destroy(id,db: Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update(id,request: schemas.Blog,db: Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#     blog.update(request.dict(),synchronize_session=False)
#     db.commit()
#     return 'updated'

# @app.post('/user',response_model= schemas.ShowUser,tags=["User"])
# def create_user(request: schemas.User,db: Session=Depends(get_db)):
   
#     new_user=models.User(name=request.name,email=request.email,password=Hash.dcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user',response_model=List[schemas.User],tags=["User"])
# def index(db: Session=Depends(get_db)):
#     user=db.query(models.User).all()
#     return user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=["User"])
# def show(id,db: Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id {id} not found')
#     return user
