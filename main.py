import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from time import strftime

# Function to update the label with current time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Format: hours:minutes:seconds AM/PM
    digital_clock.config(text=current_time)
    digital_clock.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')
root.configure(bg='black')  # Set background color to black

# Create a custom font (Roboto, 36pt, bold)
custom_font = Font(family='Roboto', size=36, weight='bold')

# Create a label widget to display the time
digital_clock = ttk.Label(root, font=custom_font, background='black', foreground='white')
digital_clock.pack(padx=20, pady=40)  # Add some padding around the clock

# Call the update_time function initially to set the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
