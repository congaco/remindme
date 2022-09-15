import tkinter

from controller.AppController import AppController
from model.AppModel import AppModel
from view.AppView import AppView


class RemindMe(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Remind Me")
        model = AppModel("")
        view = AppView(self)
        view.grid(row=0, column=0, padx=20, pady=20)
        controller = AppController(model, view)

        view.set_controller(controller)


if __name__ == "__main__":
    remindme = RemindMe()
    remindme.mainloop()
