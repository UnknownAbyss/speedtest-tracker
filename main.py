import json
import matplotlib
import tkinter as tk
import speedtest
import os

window = tk.Tk()
window.geometry("200x100")


Toggle = tk.Button(window,
        text="Show Graph of speeds",
        width=50,
        command = showGraph)

Filenames = os.listdir("./JSON")

Toggle.pack()
window.mainloop()
