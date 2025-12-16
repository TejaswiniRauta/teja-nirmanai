from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from together import Together
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",  # you can change to another model if needed
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "⚠️ Error: " + str(e)})

@app.route("/")
def home():
    return "✅ Together AI backend is running."

if __name__ == "__main__":
    app.run(debug=True)
