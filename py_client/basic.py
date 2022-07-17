import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={"abc": "144"}, json={"query": "Hello,World"}) # API Application Programming Interface

# Phone -> Camera -> App -> API -> Camera (Library API)

# REST APIs -> Web Based API -> Use HTTP
# print(response.text)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON ~ Python Dict

# Clients consumes REST APIs
print(response.json())
# print(response.status_code)