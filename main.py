import tkinter as tk
from tkinter import font
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')

        # Custom font
        self.custom_font = font.Font(family='Roboto', size=100)

        # Time label
        self.time_label = tk.Label(root, font=self.custom_font, fg='white', bg='black')
        self.time_label.pack(expand=True)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
