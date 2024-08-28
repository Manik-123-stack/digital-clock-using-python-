import tkinter as tk
from datetime import datetime
import time

class Timekeeper(tk.Tk):
    def __init__(self):
        """Initialize the main window and set up the clock and calendar displays."""
        super().__init__()
        self.title("Time and Date Tracker")
        self.geometry("320x280")

        # Frame and label for the clock display
        self.time_container = tk.Frame(self, bg='#f0f0f0')
        self.time_container.pack(pady=15)
        self.clock_display = tk.Label(self.time_container, font=('Arial', 42), fg='#333')
        self.clock_display.pack()

        # Frame and label for the calendar display
        self.date_container = tk.Frame(self, bg='#f0f0f0')
        self.date_container.pack(pady=15)
        self.date_display = tk.Label(self.date_container, font=('Arial', 24), fg='#333')
        self.date_display.pack()

        self.refresh_clock()
        self.refresh_calendar()

    def refresh_clock(self):
        """Update the time label every second."""
        current_time = time.strftime('%I:%M:%S %p')
        self.clock_display.config(text=current_time)
        self.after(1000, self.refresh_clock)  # Update every second

    def refresh_calendar(self):
        """Update the date label every minute."""
        now = datetime.now()
        current_date = now.strftime('%A, %B %d, %Y')
        self.date_display.config(text=current_date)
        self.after(60000, self.refresh_calendar)  # Update every minute

if __name__ == "__main__":
    app = Timekeeper()
    app.mainloop()