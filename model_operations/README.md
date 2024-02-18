# AIOps Model Operations

This folder containers all things model modifications and operations



- Quantisation (aka optimisation for CPU based runtimes (as opposed to GPU) by convertingn floating point to integer precision)
I put all the logic into the `download_model.py` go have a look.

The model you want to download is the q8 qantized model at `aspanner/llama-2-7b-aiopsfinetuned-q8_0-gguf` from hugging face.
You need to then rename the model and add a .bin at the end.

``` pip install huggingface_hub
python download_model-hf.py
```



