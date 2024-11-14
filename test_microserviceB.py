"""Test POST request to microservice B"""

import requests

# URL for the pdf microservice
url = 'http://127.0.0.1:5001/get_stock_data'

# Request includes url
response = requests.post(url)

# Print contents of JSON response
print(response.json())