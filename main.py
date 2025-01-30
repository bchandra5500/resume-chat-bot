import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import RAGChatbot

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize chatbot globally
resume_path = os.path.join(os.path.dirname(__file__), os.getenv("RESUME_NAME"))
try:
    chatbot = RAGChatbot(resume_path)
    print(f"Chatbot initialized successfully with resume: {resume_path}")
except Exception as e:
    print(f"Error initializing chatbot: {str(e)}")
    chatbot = None

@app.route('/chat', methods=['POST'])
def chat():
    # Log request details
    print(f"Received request: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Data: {request.get_data(as_text=True)}")
    
    if not chatbot:
        print("Error: Chatbot not initialized")
        return jsonify({
            "error": "Chatbot not initialized properly. Please check server logs."
        }), 500

    try:
        data = request.get_json()
        print(f"Parsed JSON data: {data}")
        
        if not data or 'message' not in data:
            print("Error: No message in request data")
            return jsonify({
                "error": "No message provided"
            }), 400

        user_message = data['message'].strip()
        if not user_message:
            print("Error: Empty message")
            return jsonify({
                "error": "Empty message"
            }), 400

        print(f"Processing message: {user_message}")
        response = chatbot.chat(user_message)
        print(f"Generated response: {response}")
        
        return jsonify({
            "response": response
        })

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({
            "error": f"Error processing request: {str(e)}"
        }), 500

if __name__ == "__main__":
    # Use environment variables for host/port in production
    port = int(os.environ.get("PORT", 5001))
    host = os.environ.get("HOST", "0.0.0.0")
    debug = os.environ.get("FLASK_ENV", "development") == "development"
    app.run(host=host, port=port, debug=debug)
