from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
import os
import logging
import input_guardrail

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Cerebus is RUNNING"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("text", "")
        # Call Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return jsonify({"response": response.text})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
