import tkinter
from sys import exit


class AppView(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.message_verify = None
        self.labelMessage = tkinter.Label(self, text="Message: ")
        self.labelMessage.grid(row=0, column=0)

        self.message_var = tkinter.StringVar()
        self.entry_message = tkinter.Entry(self, textvariable=self.message_var, width=100)
        self.entry_message.grid(row=0, column=1, sticky=tkinter.EW)

        self.labelTime = tkinter.Label(self, text="Time in miliseconds: ")
        self.labelTime.grid(row=1, column=0)
        self.time_var = tkinter.StringVar()
        self.entry_time = tkinter.Entry(self, textvariable=self.time_var, width=100)
        self.entry_time.grid(row=1, column=1, sticky=tkinter.EW)

        self.labelVerify = tkinter.Label(self, text="Verify: ")
        self.labelVerify.grid(row=2, column=0)
        self.verify_var = tkinter.StringVar()

        self.buttonActivate = tkinter.Button(self, text="Activate", command=self.is_activate_button_clicked)
        self.buttonActivate.grid(row=3, column=0, padx=20)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def display_notification(self, message, time):
        notification = tkinter.Tk()
        notification.after(time, exit)
        notificationGUI = tkinter.Label(notification, text=message, font=("Arial", 12), bg="green")
        notificationGUI.pack()
        return notificationGUI

    def read_content(self, file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            return content

    def is_activate_button_clicked(self):
        if self.controller:
            self.controller.save_message(self.message_var.get())
            if not self.time_var.get().isdigit():
                self.set_text_color("red")

                self.verify_var.set("Time must be integer. Please try again.")
            else:
                self.set_text_color("green")
                self.message_verify.grid(row=2, column=1, sticky=tkinter.EW)
                self.verify_var.set("Verified!")
                self.display_notification(self.read_content("messages"), self.time_var.get()).mainloop()

    def set_text_color(self,color):
        self.message_verify = tkinter.Label(self, textvariable=self.verify_var, width=100
                                            , foreground=color)
        self.message_verify.grid(row=2, column=1, sticky=tkinter.EW)