'''
**************************************************************************************

    This file is was created just for testing purpose. Kindly ignore this file.

**************************************************************************************
'''

class PerformanceTests(HttpUser):
    host = 'http://127.0.0.1:8000/Customer_details/in'
    wait_time = between(1, 3)

    @task(1)
    def testFastApi(self):    
      
        host = "http://127.0.0.1:8000/Customer_details/in"
        HEADERS = {
        "Content-Type": "application/json"
        }
        data = {
                "first_name": "enter_dummy_name",
                "last_name": "enter_dummy_last_name",
                "mobile_no": "enter_dummy_number",
                "email": "enter_dummy_email",
                "company_name": "enter_dummy_company_name",
                "city": "enter_dummy_city_name"
            }
        json_data = json.dumps(data).encode('utf8')
        response = requests.post(url=host, headers=HEADERS, data=json_data)      
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))