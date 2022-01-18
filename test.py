#Command: pytest .\test.py -sv --html report.html
import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator

schema = {
    "$schema": "https://json-schema.org/schema#",

    "type" : "object",
    "properties" : {
        "message" : {"type" : "string"},
        "timestamp": {"type" : "number"},
    }
}

def test_validate_rest_api_working():
     response = requests.get("http://localhost:3000")
     #Ensure the application is up and responds appropriately
     assert response.status_code == 200
     #Ensure correct Content-Type is set
     assert response.headers["Content-Type"] == "application/json"
     resp_body = response.json()
     #Ensure the response is what we expect
     validate(instance=resp_body, schema=schema)