# Service.py
from Models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.create(params["text"], params["Description"])