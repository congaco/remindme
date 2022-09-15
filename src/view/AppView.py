import tkinter


class AppView(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.labelMessage = tkinter.Label(self, text="Message: ")
        self.labelMessage.grid(row=0, column=0)
        self.buttonActivate = tkinter.Button(self, text="Activate", command=self.is_activate_button_clicked)
        self.buttonActivate.grid(row=1, column=0, padx=20)

        self.message_var = tkinter.StringVar()
        self.entry_message = tkinter.Entry(self, textvariable=self.message_var, width=100)
        self.entry_message.grid(row=0, column=1, sticky=tkinter.EW)


        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def is_activate_button_clicked(self):
        if self.controller:
            self.controller.save_message(self.message_var.get())

