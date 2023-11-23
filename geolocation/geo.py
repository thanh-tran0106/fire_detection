import requests

# Define the URL of the endpoint
url = "http://localhost:5000/open311/endpoint"

# Define the payload/data you want to send
data = {
    "data": "Sample request data",
    "longitude": 73.434333,  # Example longitude
    "latitude": 43.6532   # Example latitude
}

# Send the POST request
response = requests.post(url, json=data)

# Print the server's response
print(response.status_code)
print(response.json())

