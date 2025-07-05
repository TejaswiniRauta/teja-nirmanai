from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"
    }

    data = {
        "inputs": user_input
    }

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-small",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            output = response.json()
            print("✅ Output:", output)
            return jsonify({"reply": output[0]["generated_text"]})
        else:
            print("⚠️ Error Response:", response.text)
            return jsonify({"reply": "⚠️ Error: " + response.text})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Exception: {str(e)}"})

@app.route("/")
def home():
    return "✅ Hugging Face backend is running."

if __name__ == "__main__":
    app.run(debug=True)

