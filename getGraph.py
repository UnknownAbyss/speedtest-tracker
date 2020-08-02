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
        plt.xlabel("Intervals")
        plt.ylabel("Speeds in Mbps")
        plt.show()
    else:
        pass

#Button which on press calls ShowGraph function
Toggle = tk.Button(window,
        text="Show Graph of speeds",
        width=50,
        command = ShowGraph,)

#List of all files in JSON folder
Filenames = tk.Label(window,
        text="\n".join(os.listdir("./JSON")))

#Textbox to put filename in
FileLabel = tk.Label(window,
        text="Filename:")
File = tk.Entry(window)



Toggle.pack()
FileLabel.pack(side = tk.LEFT)
File.pack(side = tk.RIGHT)
Filenames.pack()
window.mainloop()
