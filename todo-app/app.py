import os
from flask import Flask
# Import your blueprint from a separate module
from routes import todo


app = Flask(__name__)

app.register_blueprint(todo)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)