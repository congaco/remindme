class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save_message(self, message):
        self.model.message = message
        self.model.save_message()

    def read_content(self, file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            return content
