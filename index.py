from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

BASE_URL = "https://gemini.discord.rocks/vision"

@app.route('/')
def home():
    return '<h1>Hello World</h1>'

@app.route('/image/vision', methods=['POST'])
def vision_endpoint():
    try:
        data = request.json
        image_url = data.get('url')
        question = data.get('question')

        print(data, image_url)

        if image_url is None or question is None:
            return jsonify({"error": "Missing 'url' or 'question' in the request body"}), 400

        payload = {
            "url": image_url,
            "question": question
        }

        try:
            response = requests.post(BASE_URL, json=payload)
            return jsonify(response.json())
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)
