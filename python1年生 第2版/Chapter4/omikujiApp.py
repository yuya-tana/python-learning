import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉","中吉","吉","凶",]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("500x300")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()

