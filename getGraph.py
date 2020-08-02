import json
import matplotlib.pyplot as plt
import tkinter as tk
import os

window = tk.Tk()


def ShowGraph():
    fname = File.get()
    f = open("./JSON/"+fname, "r+")
    ftext = json.load(f)
    fdict = json.loads(ftext)
    print(fdict, type(fdict))
    if fdict:
        plt.plot(fdict.keys(), fdict.values())
        plt.show()
    else:
        pass


Toggle = tk.Button(window,
        text="Show Graph of speeds",
        width=50,
        command = ShowGraph,)

Filenames = tk.Label(window,
        text="\n".join(os.listdir("./JSON")))

FileLabel = tk.Label(window,
        text="Filename:")

File = tk.Entry(window)



Toggle.pack()
FileLabel.pack(side = tk.LEFT)
File.pack(side = tk.RIGHT)
Filenames.pack()
window.mainloop()
