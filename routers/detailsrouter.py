from fastapi import APIRouter, Depends, Response, status, Request
from database import  get_db
from sqlalchemy.orm import Session
import database, schemas
import repository
from repository import detailsrepo

router=APIRouter(                   #creating a router i.e APIRouter which is inbuilt mopdule of FastAPI
    prefix='/Customer_details',
    tags=['Customer'],
    
    )

@router.post('/in') #post method
def insert_detail(request:schemas.customer,db:Session=Depends(database.get_db)):
    return detailsrepo.create(request, db)

@router.get('/') #get method
def all_detail(db:Session=Depends(get_db)):
    return detailsrepo.showing_details(db)

@router.put('/update_details/{give_id}', status_code=status.HTTP_202_ACCEPTED) #put method/update method
def update(give_id,request: schemas.customer, db:Session=Depends(get_db)):
    return detailsrepo.updated_details(give_id, request, db)

@router.delete('/delete/{give_id}', status_code=status.HTTP_404_NOT_FOUND) #delete method
def destroy(give_id, db:Session=Depends(get_db)):
    return detailsrepo.delete_details(give_id, db)