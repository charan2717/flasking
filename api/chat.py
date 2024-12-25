from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    # Simple response logic
    response_message = f"You said: {user_message}"
    return jsonify({"response": response_message})
