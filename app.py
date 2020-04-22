# app.py

from flask import Flask
from Models import Schema
from Service import ToDoService

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello {name}"

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

if __name__ == "__main__":
    Schema()
    app.run(debug=True)