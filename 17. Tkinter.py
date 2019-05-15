import tkinter as tk
root=tk.Tk()
tk.Label(root,
         text="Buzz",
         fg="red",
         font="Times 40 bold").pack()

tk.Label(root,
         text="Meow",
         fg="green",
         font="Helvetica 30 bold italic").pack()

tk.Label(root,
         text="Bhau",
         fg="blue",
         bg="yellow",
         font="Verdana 20 bold italic").pack()
root.mainloop()
