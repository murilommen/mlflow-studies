import requests

result = requests.get("http://localhost:5000/?msg=HelloFromGET")

print(result.json())

result = requests.post('http://localhost:5000/', 
                       json={'msg': 'Hello from POST'})

print(result.json())