# AIOps

Global engineering AI Combinator Hackathon

To Run the Flask application:
    
     python slack-api.py

To send slack message : 

    curl -H 'Content-Type: application/json' --data  '{"slack_id":"Hello, send aiops message!"}' -X POST http://localhost:5000/send-to-slack

