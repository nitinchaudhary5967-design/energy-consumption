# genai/infer.py (pseudocode)
import requests, json

def generate_insights(summary_text, api_key):
    url = "https://api.example-genai.com/v1/generate"
    prompt = f"Summarize these electricity consumption insights:\n\n{summary_text}\n\nMake 4 action points."
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}
    resp = requests.post(url, json={"prompt":prompt, "max_tokens":300}, headers=headers)
    return resp.json()

# prepare a small text summary from data:
summary_text = "Avg daily consumption 25 kWh, peak hours 18-21, frequent spikes on weekdays..."
# call:
# insights = generate_insights(summary_text, "YOUR_API_KEY")
# print(insights)
