from huggingface_hub import snapshot_download

model_id="aspanner/llama-2-7b-aiopsfinetuned"

snapshot_download(repo_id=model_id, local_dir="aiopsmodel-hf", local_dir_use_symlinks=False, revision="main")
