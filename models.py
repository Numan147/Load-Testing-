'''
models.py file to store our API model
'''

from enum import unique
from multiprocessing.spawn import import_main_path
from sqlalchemy import Column, Integer, String
from database import Base

class Cdetails(Base): #creating model by defining class.
    __tablename__ = 'YOU_TABLE_NAME' #defining table name so that after connecting to database details inserted by user will get saved in this perticular table only. 

    id=Column(Integer, primary_key=True, index=True) #letting our API know which all columns out DB table consist and its datatype
    first_name=Column(String)
    last_name=Column(String)
    mobile_no=Column(Integer, unique=True)
    email=Column(String)
    company_name=Column(String)
    city=Column(String)
