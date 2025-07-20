# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Get a message from an environment variable, or use a default
    message = os.environ.get('GREETING_MESSAGE', 'Hello from Flask!')
    return f"<h1>{message}</h1><p>Running on port {os.environ.get('PORT', '5000')}</p>"

if __name__ == '__main__':
    # Get port from environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)