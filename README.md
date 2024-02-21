# AIOps

As part our 2024 Global engineering AI Combinator Hackathon I submitted the idea to create AI aided support for our platforms like OpenShift (including SNO), RHEL (incl RHDE) and MicroShift.
The process was to follow the recommended way for any AI project to go end-to-end and not just focusing on one particular area. So we went through Data Engineering -> Model Training -> Model Deployment and running inference.
![image](https://github.com/aspanner/AIOps/assets/16040521/1b8ffce8-c078-4d35-b749-0895ddef4909)

We went through several architecture iterations, with each iteration making it simpler in order to be able to finish a run-through end-to-end.
We ended up with this architecture which the implementation of this repository represents:
![image](https://github.com/aspanner/AIOps/assets/16040521/73d57978-dbfd-4a16-ab12-9e5c3d7a5eac)




To get things run you need to clone this repo, download the model from hf (hugging face) as descried in the model operations folder.
If you get stuck with the model you can download the quantized version directly from hf from ` https://huggingface.co/aspanner/llama-2-7b-aiopsfinetuned-q8_0-gguf `

- I recommend to create and activea a python virtual environment, as llama.cpp, huggingface, streamlit an other components might clash with things you already got installed.
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
Your zsh prompt should show the activated virtual environment name - below on the right hand side:
![image](https://github.com/aspanner/AIOps/assets/16040521/769659ec-b9d3-4249-8485-1fef1af5e493)

Then upgrade your pip via ` pip install --upgrade pip `

Then run ` pip install -r requirements.txt `

Then run ` streamlit run app.py ` from this folder and you should be greeted by a UI like this:
![image](https://github.com/aspanner/AIOps/assets/16040521/1ae164b6-6e69-4663-aa16-3daae475d769)


# Additional non-core items
#Slack Integration
I've moved all the slack integration work into the subfolder 'slack_integration'

To send slack message : 

    curl -H 'Content-Type: application/json' --data  '{"slack_id":"Hello, send aiops message!"}' -X POST http://localhost:5000/send-to-slack

