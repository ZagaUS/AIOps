from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send-to-slack', methods=['POST'])
def send_to_slack():
    data = request.json  # Assuming you're sending JSON data
    slack_id = data.get('slack_id')

    if not slack_id:
        return jsonify({'error': 'slack_id is required'}), 400

    # Replace 'YOUR_SLACK_WEBHOOK_URL' with your actual Slack webhook URL
    # slack_webhook_url = 'YOUR_SLACK_WEBHOOK_URL'
    slack_webhook_url = 'https://hooks.slack.com/services/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'

    payload = {
        'text': f'Slack ID: {slack_id}'
    }

    response = requests.post(slack_webhook_url, json=payload)

    if response.ok:
        return jsonify({'message': 'Message sent to Slack successfully'})
    else:
        return jsonify({'error': 'Failed to send message to Slack'}), 500

if __name__ == '__main__':
    app.run(port=5001,debug=True)
