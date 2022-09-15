
class AppModel:
    def __init__(self, message):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, content):
        self.__message = content

    def save_message(self):
        with open("messages", "a") as f:
            f.write(self.message)
            f.write("\n")
