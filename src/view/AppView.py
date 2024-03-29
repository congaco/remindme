import tkinter
from sys import exit


class AppView(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.notification = None


        self.message_verify = None
        self.labelMessage = tkinter.Label(self, text="Message: ")  # save messages in combox for more messages
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
        notification.after_idle(time, self.appear())
        notificationGUI = tkinter.Label(notification, text=message, font=("Arial", 12), bg="green")
        notificationGUI.pack()
        return notificationGUI

    def set_message_notification(self):
        tkinter.Label(self.notification, text=self.controller.read_content("messages"), font=("Arial", 12),
                      bg="green").place(x=10, y=10)

    def disappear(self):
        self.set_message_notification()
        self.notification.withdraw()
        if self.time_var.get().isdigit():
            self.notification.after(int(self.time_var.get()), self.appear)

    def appear(self):
        self.set_message_notification()
        self.notification.deiconify()
        if self.time_var.get().isdigit():
            self.notification.after(int(self.time_var.get()), self.disappear)

    def start(self):
        self.notification = tkinter.Tk()
        tkinter.Frame(self.notification, width=250, height=100).pack()
        self.notification.after_idle(self.appear)
        self.notification.mainloop()

    def is_activate_button_clicked(self):
        if self.controller:
            self.controller.save_message(self.message_var.get())
            if not self.time_var.get().isdigit():
                self.set_verified_message("red")
                self.verify_var.set("Time must be integer. Please try again.")
            else:
                self.set_verified_message("green")
                self.message_verify.grid(row=2, column=1, sticky=tkinter.EW)
                self.verify_var.set("Verified!")
                self.start()

    def set_verified_message(self, color):
        self.message_verify = tkinter.Label(self, textvariable=self.verify_var, width=100, foreground=color)
        self.message_verify.grid(row=2, column=1, sticky=tkinter.EW)
