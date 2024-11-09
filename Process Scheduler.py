import tkinter as tk
from tkinter import ttk, messagebox

# Process Class
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time  # For Round Robin
        self.start_time = None
        self.end_time = None

    def reset(self):
        """Reset process attributes for a fresh simulation."""
        self.remaining_time = self.burst_time
        self.start_time = None
        self.end_time = None
    
    def __str__(self):
        return (f"PID:{self.pid}, Arrival: {self.arrival_time},"
                f"Burst: {self.burst_time}, Priority: {self.priority}")