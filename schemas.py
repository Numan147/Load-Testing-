'''
schemas file to store out schemas for API
'''

from fastapi import FastAPI
from pydantic import BaseModel

class customer(BaseModel): #creating a class customer (BaseModel) for out schema to store records which are given by the user.
    first_name:str #defining datatype 
    last_name:str
    mobile_no: str
    email:str
    company_name:str
    city:str


class orm():
    orm_mode=True