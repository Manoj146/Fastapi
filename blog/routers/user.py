from fastapi import APIRouter,Depends
from .. import schemas,database
from typing import List 
from sqlalchemy.orm import Session 
from ..repository import user


router=APIRouter(
    prefix='/users',
    tags=['Users']
)

get_db=database.get_db

@router.post('/',response_model= schemas.ShowUser)
def create_user(request: schemas.User,db: Session=Depends(get_db)):
    user.create(request,db)

@router.get('/',response_model=List[schemas.User])
def index(db: Session=Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}',response_model=schemas.ShowUser)
def show(id,db: Session=Depends(get_db)):
    return user.show(id,db)
