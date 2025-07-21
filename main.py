from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    message = os.environ.get('GREETING_MESSAGE', 'Hello from Flask!')
    return f"<h1>{message}</h1><p>Running on port {os.environ.get('PORT', '5050')}</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)