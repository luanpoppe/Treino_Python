import tkinter as tk
from tkinter import ttk
from PyPDF2 import PdfReader
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.title("Testezera 01")
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
ttk.Label(frm, background="red", text="SIMBORA IRMÃO").grid(column=1, row=2)

root.mainloop()