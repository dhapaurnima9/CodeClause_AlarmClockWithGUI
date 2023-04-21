import tkinter as tk
import datetime
import time
from tkinter import messagebox

# Function to set the alarm
def set_alarm():
    alarm_time = entry_time.get()
    alarm_message = entry_message.get()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        root.update()
        time.sleep(1)

    # Show alarm message when the alarm goes off
    messagebox.showinfo("Alarm", alarm_message)

# Create main window
root = tk.Tk()
root.title("Alarm Clock")

# Create GUI components
label_time = tk.Label(root, text="Set Alarm Time (HH:MM:SS):")
label_time.pack()
entry_time = tk.Entry(root)
entry_time.pack()
label_message = tk.Label(root, text="Enter Alarm Message:")
label_message.pack()
entry_message = tk.Entry(root)
entry_message.pack()
button_set = tk.Button(root, text="Set Alarm", command=set_alarm)
button_set.pack()

# Run main loop
root.mainloop()
