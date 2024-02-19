import subprocess
import configparser
import requests
import json
from datetime import datetime

slack_gateway_url = 'http://127.0.0.1:5001/send-to-slack'



def constructJsonPayload (jsonpayload):
    payload = {
        'slack_id' : f'{jsonpayload}'
    }

    return payload

def monitor_journalctl(keywords):
    # Run the journalctl command with the '-f' option to follow the journal
    process = subprocess.Popen(['journalctl', '-f'], stdout=subprocess.PIPE)

    # Continuously monitor the output and print new lines
    while True:
        # Read a line from the journalctl output
        line = process.stdout.readline()

        # Decode the line from bytes to string
        line = line.decode('utf-8')

        # Check if the line contains any of the specified keywords
        if any(keyword in line for keyword in keywords):
            # Print the line
            print(line.strip())
           
            ##add code to forward to LLLM/RAG/VectorDB
            
            
            ###forwarding AiOps responses to slack
            jsonPayload = constructJsonPayload(line.strip())
            send2slack(slack_gateway_url,jsonPayload)
    


def send2slack(url, payload):
    response = requests.post(url, json=payload)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.json())
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        print(response.text)  

    

if __name__ == "__main__":
    config=configparser.ConfigParser()
    config.read('./../config.ini')
    print(config.sections())
    webhook=config['SLACK']['slack_webhook']
    print("substringed webhook:" + webhook[:45])
    
    # inititalising slack gateway (aka a rest service server)
    # Define the URL of the REST API endpoint
    
    payloadMessage ="Initalizing slack integration: Message from AIOps to slack at " + str(datetime.now())

    payload = {
        'slack_id' : f'{payloadMessage}'
    }
    
    send2slack(slack_gateway_url,payload)

    # Specify the keywords you want to filter by
    keywords = ["microshift", "audit"]

    # Start monitoring journalctl with the specified keywords
    monitor_journalctl(keywords)







    
    
