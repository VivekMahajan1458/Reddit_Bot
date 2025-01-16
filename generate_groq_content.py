import requests
import config

def generate_groq_content(prompt):
    headers = {"Authorization": f"Bearer {config.GROQ_API_KEY}"}
    data = {"prompt": prompt}
    response = requests.post(config.GROQ_API_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()['text']
