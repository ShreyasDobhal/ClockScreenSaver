import tkinter as tk
from tkinter import font
import time
import calendar
from datetime import datetime

CAL_SIZE = [600, 400]

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')

        # Bind the mouse click event to close the window
        # self.root.bind("<Button-1>", self.close_window)
        # Bind various events to close the window
        self.root.bind("<Button-1>", self.close_window)  # Mouse click
        self.root.bind("<Key>", self.close_window)       # Key press
        self.root.bind("<Motion>", self.close_window)    # Mouse movement

        # Custom font
        self.custom_font = font.Font(family='Roboto', size=100)
        self.calendar_font = font.Font(family='Roboto', size=16)

        # Canvas for precise text placement
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Draw calendar and clock
        self.draw_calendar()
        

        self.update_clock()

    def draw_calendar(self, align="right"):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        cal = calendar.monthcalendar(year, month)
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        cal_width = self.root.winfo_screenwidth() // 4.5
        cal_height = self.root.winfo_screenheight() // 4.5
        if align == 'right':
            x_start = self.root.winfo_screenwidth() * 3 // 4 - cal_width // 2
        elif align == 'left':
            x_start = self.root.winfo_screenwidth() // 4 - cal_width // 2
        else:
            x_start = self.root.winfo_screenwidth() // 2 - cal_width // 2

        y_start = 200

        # Draw rectangle for the calendar background
        self.canvas.create_rectangle(
            x_start, y_start,
            x_start + cal_width, y_start + cal_height,
            fill='#555555', outline='', width=0, stipple='gray50'
        )

        cell_width = cal_width // 7
        cell_height = cal_height // (len(cal) + 1)

        # Draw the day of week headers
        for i, day_name in enumerate(days_of_week):
            self.canvas.create_text(
                x_start + i * cell_width + cell_width // 2, 
                y_start + cell_height // 2,
                text=day_name,
                font=self.calendar_font,
                fill='white'
            )

        # Draw the days
        for r, week in enumerate(cal):
            for c, day_num in enumerate(week):
                if day_num != 0:
                    x = x_start + c * cell_width + cell_width // 2
                    y = y_start + (r + 1) * cell_height + cell_height // 2
                    self.canvas.create_text(
                        x, y,
                        text=str(day_num),
                        font=self.calendar_font,
                        fill='white'
                    )
                    if day_num == day:
                        self.canvas.create_rectangle(
                            x - cell_width // 2 + 3, y - cell_height // 2 + 1,
                            x + cell_width // 2 - 3, y + cell_height // 2 - 1,
                            outline='white', width=2
                        )
        
        if align == 'right':
            x_start = self.root.winfo_screenwidth() * 3 // 4
        elif align == 'left':
            x_start = self.root.winfo_screenwidth() // 4
        else:
            x_start = self.root.winfo_screenwidth() // 2

        self.time_text_id = self.canvas.create_text(
            x_start,
            y_start + cell_height + 300,
            font=self.custom_font, 
            fill='white',
            text=""
        )

    def update_clock(self):
        current_time = time.strftime("%H:%M")
        self.canvas.itemconfig(self.time_text_id, text=current_time)
        self.root.after(60000, self.update_clock)

    def close_window(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
