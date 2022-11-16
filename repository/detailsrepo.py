from ast import Num
import email
from email.message import EmailMessage
from http.client import HTTP_PORT
import numbers
from pyexpat import model
from tkinter import N
from typing import Union
import re
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
import  models
from fastapi import Depends, Response,status, HTTPException, Request, Query
import schemas
from pydantic import BaseModel

def create(request, db:Session):  #defining a function 'create' to post and store data given by user into database which gets executed in post method in detailsrouter.py file.
    '''
    **************************************************************************************
    UNCOMMENT THIS SECTION ONLY WHILE LOADTESTING (GET) METHOD, OR WHILE VALIDTATING DATA.
    **************************************************************************************
    # name_validate(request) #these are all defination function to validate data by user as per API standard
    # number_validate(request) 
    # email_validate(request)
    # dup_email(request, db)
    '''
    test=models.Cdetails(first_name=request.first_name,   
                        last_name=request.last_name, 
                        mobile_no= request.mobile_no,
                        email=request.email,
                        company_name=request.company_name,
                        city=request.city)
    db.add(test)
    db.commit()
    db.refresh(test)    
    msg = { #giving msg that our post method got executed successfully this is known as dictionary
            "Status":"Success", 
            "Details":test  
        }
    return msg

def name_validate(request:schemas.customer):  #Function to validate name.
    reg_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE) #By using regular expression
    lname=request.last_name
    fname=request.first_name
    if(reg_name.match(lname)) and (reg_name.match(fname)): #using if else statment to validate
        return 'Valid Name'
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail= f'Invalid First or Last Name Entry') #if not valid raising exception.
    
def email_validate(request:schemas.customer): #function to validate email 
    reg_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b') #by using regular expression
    emails=request.email
    if(reg_email.match(emails)):
        return 'valid email'
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'Invalid Email Entry') #if not valid raising exception.

def dup_email(request:schemas.customer, db:Session): #function to validate duplicate email. #no duplicate email allowed
    email1=request.email
    duplicate_email=db.query(models.Cdetails).filter(models.Cdetails.email==email1).first()
    if duplicate_email:

        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Duplicate email entry not allowed') #if not valid raising exception.
    else:
        return 'successfull'

      
def number_validate(request:schemas.customer): #Function to validate mobile number as per our API Standard
    reg_num=re.compile('(0|91)?[6-9][0-9]{9}') #by using regular expression.
    number=request.mobile_no
    if(reg_num.match(number)):
        return 'Valid Number'
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail = f"Invalid Mobile Number Entry.") #if not valid raising exception.


def showing_details(db:Session=Depends(get_db)): #function to show details.
    details=db.query(models.Cdetails).all() #.all is used to show all the details user has passed into database
    return details

def updated_details(insert_id, request: schemas.customer, db:Session=Depends(get_db)): #function to update details.
    insert = db.query(models.Cdetails).filter(models.Cdetails.id==insert_id)
    if not insert.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, #raising exception error if the details which needs to be updated is not present in DB
                            detail = f"Details not found.")
    insert.update(request.dict())
    db.commit()
    return {f'Record with ID. {insert_id} has been updated'}

def delete_details(give_id, db: Session=Depends(get_db)): #delete function to deleted records present in DB.
    des_details = db.query(models.Cdetails).filter(models.Cdetails.id==give_id)
    if not des_details.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, #raising exception error if the details which needs to be deleted is not present in DB
                            detail = f"Details for id {give_id} not found.")
    des_details.delete(synchronize_session=False)
    db.commit()
    return{f'Record with ID {give_id} has been deleted successfully.'}