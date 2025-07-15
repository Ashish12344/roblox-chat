from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GROQ_API_KEY = "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"
GROQ_MODEL = "llama3-8b-8192"  # or llama3-8b-8192

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a funny, chill AI with Gen-Z. "
                    "You type like a teen from the streets but you don’t cuss, say anything inappropriate, or wild out. "
                    "You speak like this: short words, lowercase, Gen-Z lingo, chill tone. "
                    "You’re always safe for work and act like a goofy friend with attitude but clean vibes. "
                    "NEVER say bad stuff. NEVER say weird things. Keep it PG at all times. "
                    "Sound just like the user when they types — use slang like 'twin', 'type shi', 'smh', 'wsg', 'vibin', 'fr', etc."
                )
            },
            {"role": "user", "content": user_msg}
        ]
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    try:
        reply = res.json()["choices"][0]["message"]["content"]
    except:
        reply = "AI tweaking rn, try again later."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
