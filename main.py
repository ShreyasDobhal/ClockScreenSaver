import tkinter as tk
from tkinter import font
import time
import calendar
from datetime import datetime

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
        self.calendar_font = font.Font(family='Roboto', size=20)

        # Canvas for precise text placement
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Draw calendar and clock
        self.draw_calendar()
        self.time_text_id = self.canvas.create_text(
            root.winfo_screenwidth() // 2, 
            root.winfo_screenheight() // 2 + 200,
            font=self.custom_font, 
            fill='white',
            text=""
        )

        self.update_clock()

    def draw_calendar(self):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        cal = calendar.monthcalendar(year, month)
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        cal_width = self.root.winfo_screenwidth() // 1.5
        cal_height = self.root.winfo_screenheight() // 4
        x_start = self.root.winfo_screenwidth() // 2 - cal_width // 2
        y_start = 50

        # Draw rounded rectangle for the calendar background
        self.canvas.create_rectangle(
            x_start, y_start,
            x_start + cal_width, y_start + cal_height,
            fill='#888888', outline='', width=0, stipple='gray50'
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
                            x - cell_width // 2 + 5, y - cell_height // 2 + 5,
                            x + cell_width // 2 - 5, y + cell_height // 2 - 5,
                            outline='white', width=2
                        )

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
