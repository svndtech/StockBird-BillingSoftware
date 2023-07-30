import tkinter as tk
from .Components import login

class rootGui:
    
    def __init__(self) -> None:
        self.root = tk.Tk()

    def getRoot(self):
        return self.root

    def mainLoop(self):
        self.root.mainloop()

    def getLoginFrame(self):
        login_component = login.loginComponent()
        login_component.pack()
        self.root.mainloop()

