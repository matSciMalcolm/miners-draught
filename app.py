# app.py

from flask import Flask
from models import Schema

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello {name}"

if __name__ == "__main__":
    Schema()
    app.run(debug=True)