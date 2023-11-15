import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        display_image(img)

def display_image(image):
    img.thumbnail((300, 300))  # Resize the image for display purposes
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk  # Keep a reference to avoid garbage collection

root = tk.Tk()
root.title("Simple Image Viewer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

open_button = tk.Button(frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT)

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

root.mainloop()
