import tkinter as tk
from tkinter import font
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')

        # Bind the mouse click event to close the window
        self.root.bind("<Button-1>", self.close_window)

        # Custom font
        self.custom_font = font.Font(family='Roboto', size=100)

        # Canvas for precise text placement
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Time text ID
        self.time_text_id = self.canvas.create_text(
            root.winfo_screenwidth() // 2, 
            root.winfo_screenheight() // 2,
            font=self.custom_font, 
            fill='white',
            text=""
        )

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.canvas.itemconfig(self.time_text_id, text=current_time)
        self.root.after(1000, self.update_clock)

    def close_window(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
