'''
This is the main file of the kids game app.
'''
import tkinter as tk
from game import Game
class KidsGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kids Game App")
        self.geometry("800x600")
        self.game = Game(self)
        self.game.pack()
if __name__ == "__main__":
    app = KidsGameApp()
    app.mainloop()