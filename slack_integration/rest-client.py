import requests

# Define the URL of the REST API endpoint
url = 'http://127.0.0.1:5001/send-to-slack'

payload = {
    'slack_id' : 'Message from AIOps to Andreas!'
}

response = requests.post(url, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
    print(response.text)  
