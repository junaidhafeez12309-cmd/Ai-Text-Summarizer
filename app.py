from flask import Flask, render_template, request,send_from_directory
from transformers import pipeline

app = Flask(__name__)

# Supported model options (key => HF model id and optional input prefix)
MODEL_OPTIONS = {
    "t5-small": {"id": "t5-small", "prefix": "summarize: "},
    "bart-large-cnn": {"id": "facebook/bart-large-cnn", "prefix": ""},
    "pegasus-xsum": {"id": "google/pegasus-xsum", "prefix": ""},
}

# Cache loaded pipelines per model to avoid reloading each request
_pipeline_cache = {}


def _load_summarizer_with_fallback(model_name="t5-small"):
    task_candidates = ["summarization", "text2text-generation", "text-generation", "any-to-any", "image-text-to-text"]
    for task in task_candidates:
        try:
            return pipeline(task, model=model_name, tokenizer=model_name)
        except Exception:
            continue
    raise RuntimeError("No supported pipeline task found in this Transformers installation.")


def get_summarizer_for(model_key: str):
    info = MODEL_OPTIONS.get(model_key)
    if info is None:
        info = MODEL_OPTIONS["t5-small"]
    model_id = info["id"]
    if model_id in _pipeline_cache:
        return _pipeline_cache[model_id], info.get("prefix", "")
    pipe = _load_summarizer_with_fallback(model_id)
    _pipeline_cache[model_id] = pipe
    return pipe, info.get("prefix", "")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/summarize')
def summarize():
    return render_template('summarizepage.html')

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    text = request.form['text']
    model_key = request.form.get('model', 't5-small')

    # AI summarization
    summarizer, prefix = get_summarizer_for(model_key)
    prompt = prefix + text
    result = summarizer(prompt, max_length=60, min_length=20, do_sample=False)
    summary = result[0].get('generated_text', result[0].get('summary_text', ''))

    return summary
@app.route('/sw.js')
def monetag_sw():
    return send_from_directory('.', 'sw.js')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)