import imp
from urllib import request
from locust import User, TaskSet, HttpUser
from locust import User, task, between, constant
from locust import HttpUser, task
import json
import random

class PerformanceTests(HttpUser):
    wait_time = between(1, 3) # seconds between requests to perform the test and wait for the test to complete.

    @task(1)
    def testFastApi(self):   
      
        host = 'http://127.0.0.1:8000/Customer_details/in' #note: host is for the specific file structure when you clone on your local machine.
        HEADERS = {
        "Content-Type": "application/json"
        }
        #this is a static data to be filled by user. And which will repeatedly be inserted into the database. 
        data = [{
                "first_name": "enter_dummy_name",
                "last_name": "enter_dummy_last_name",
                "mobile_no": "enter_dummy_number",
                "email": "enter_dummy_email",
                "company_name": "enter_dummy_company_name",
                "city": "enter_dummy_city_name"
            },
            {
                "first_name": "enter_dummy_name",
                "last_name": "enter_dummy_last_name",
                "mobile_no": "enter_dummy_number",
                "email": "enter_dummy_email",
                "company_name": "enter_dummy_company_name",
                "city": "enter_dummy_city_name"
            },
            {
                "first_name": "enter_dummy_name",
                "last_name": "enter_dummy_last_name",
                "mobile_no": "enter_dummy_number",
                "email": "enter_dummy_email",
                "company_name": "enter_dummy_company_name",
                "city": "enter_dummy_city_name"
            },
            {
                "first_name": "enter_dummy_name",
                "last_name": "enter_dummy_last_name",
                "mobile_no": "enter_dummy_number",
                "email": "enter_dummy_email",
                "company_name": "enter_dummy_company_name",
                "city": "enter_dummy_city_name"
            }]

        #json_data = json.dumps(data).encode('utf8')
        result1 = random.choice(data)
        json_data = json.dumps(result1).encode('utf8')
        response = self.client.post(url=host, headers=HEADERS, data = json_data) 
        print(result1)     

        
        
