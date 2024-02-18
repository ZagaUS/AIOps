# AIOps

Global engineering AI Combinator Hackathon

To get things run you need to clone this repo, download the model from hf (hugging face) as descried in the model operations folder.

- Recommended
I recommend to create and activea a python virtual environment, as llama.cpp, huggingface, streamlit an other components might clash.
To do that run (aiopsVE is the name of my virttual environment(VE):
' python3.12 -m venv aiopsVE '
and then activate it with
' source aiopsVE/bin/activate'

if you do a 'pip list' you should see an empty list, meaning no pip packags are install yet.

```
❯ pip list
Package Version
------- -------
pip     23.2.1

[notice] A new release of pip is available: 23.2.1 -> 24.0
[notice] To update, run: pip install --upgrade pip
```
Your zsh prompt should so the activated virtual environment name - below on the right hand side:
![image](https://github.com/aspanner/AIOps/assets/16040521/769659ec-b9d3-4249-8485-1fef1af5e493)

Then upgrade your pip via ` pip install --upgrade pip `

Then run ` pip install -r requirements.txt `

Then run ` streamlit run app.py ` from this folder and you should be greeted by a UI like this:
![image](https://github.com/aspanner/AIOps/assets/16040521/1ae164b6-6e69-4663-aa16-3daae475d769)


# Additional non-core items
#Slack Integration
To Run the Flask application:
    
     python slack-api.py

To send slack message : 

    curl -H 'Content-Type: application/json' --data  '{"slack_id":"Hello, send aiops message!"}' -X POST http://localhost:5000/send-to-slack

