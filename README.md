# AI Text Summarizer

Simple Flask app that summarizes text using Hugging Face transformer models.

## Features
- Paste long text and get a short summary
- Choose between three models: `t5-small`, `facebook/bart-large-cnn`, `google/pegasus-xsum`

## Prerequisites
- Python 3.10 or newer
- pip
- (optional) a Hugging Face token for higher rate limits and faster downloads

## Install
Create and activate a virtual environment (recommended), then install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
pip install --upgrade pip
pip install flask transformers torch sentencepiece
```

Or if you prefer a single command (may install CPU or GPU builds of torch depending on platform):

```powershell
pip install flask transformers torch sentencepiece
```

## Run
Set your HF token (optional but recommended):

```powershell
$env:HF_TOKEN='your_token_here'
python app.py
```

Open http://localhost:5000/summarize in your browser.

## Models
- `t5-small` — small and fast, good for demos
- `facebook/bart-large-cnn` — accurate general-purpose summarization
- `google/pegasus-xsum` — tuned for news-style summaries

Select a model from the UI before summarizing. The first time a model is used it will be downloaded (this can be large).

## Troubleshooting
- If you see errors about unknown pipeline tasks, update `transformers`:

```powershell
pip install -U transformers
```

- If model downloads are slow or rate limited, set `HF_TOKEN` as shown above.

- If the app fails to start, run `python app.py` from the project root and paste the error here for help.

## Files changed/created
- [app.py](app.py) — added model selection and pipeline fallback logic
- [templates/summarizepage.html](templates/summarizepage.html) — added model selector
- [static/js/summarize.js](static/js/summarize.js) — send model choice with requests
- [README.md](README.md) — this file

---
If you want, I can create a `requirements.txt` and try starting the app here to confirm everything runs.