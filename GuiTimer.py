import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from TimerController import TimerController, TimerView

# Fixed up from AI generated code
# See https://chat.openai.com/share/d3a6bacd-959a-4762-a608-8e67a3fc6e90

class GuiTimer(TimerView):
    def __init__(self):
        self.controller = TimerController(self)
        self.root = tk.Tk()
        self.root.title("Timer")
        
        self.minutes = 0
        self.seconds = 0
        
        self.timer_label = ttk.Label(self.root, text="00:00")
        self.timer_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.start_button = ttk.Button(self.root, text="Start", command=self.start)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.controller.stop)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)
        
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.controller.pause)
        self.pause_button.grid(row=1, column=2, padx=5, pady=5)
        
        self.resume_button = ttk.Button(self.root, text="Resume", command=self.controller.resume)
        self.resume_button.grid(row=1, column=3, padx=5, pady=5)
        
        self.minutes_up_button = ttk.Button(self.root, text="▲", command=self.increment_minutes)
        self.minutes_up_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.minutes_down_button = ttk.Button(self.root, text="▼", command=self.decrement_minutes)
        self.minutes_down_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.seconds_up_button = ttk.Button(self.root, text="▲", command=self.increment_seconds)
        self.seconds_up_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.seconds_down_button = ttk.Button(self.root, text="▼", command=self.decrement_seconds)
        self.seconds_down_button.grid(row=3, column=1, padx=5, pady=5)
        
        
    def increment_minutes(self):
        self.minutes += 1
        self.display_time()
        
    def decrement_minutes(self):
        if self.minutes > 0:
            self.minutes -= 1
            self.display_time()
        
    def increment_seconds(self):
        self.seconds += 5
        if self.seconds >= 60:
            self.seconds = 0
            self.increment_minutes()
        self.display_time()
        
    def decrement_seconds(self):
        if self.seconds >= 5:
            self.seconds -= 5
        else:
            if self.minutes > 0:
                self.minutes -= 1
                self.seconds = 55
            else:
                self.seconds = 0
        self.display_time()
        
    def display_time(self):
        time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.timer_label.config(text=time_str)

    def update_time(self, time_in_seconds):
        self.minutes = time_in_seconds // 60
        self.seconds = time_in_seconds % 60
        self.display_time()

    def timer_done(self):
        pass
        
    def start(self):
        time_in_seconds = 60*self.minutes + self.seconds
        self.controller.start(time_in_seconds)
        
    def stop(self):
        self.controller.stop()
        
    def pause(self):
        self.controller.pause()
        
    def resume(self):
        self.controller.resume()
        
    def run(self):
        self.root.mainloop()

# Example usage:
if __name__ == "__main__":
    GuiTimer().run()

