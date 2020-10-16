
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import subprocess

def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png"),("jpg files", "*.jpg")))
    basewidth = 800 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()

def classify():
    global img, image_data
    import subprocess
    for img_display in frame.winfo_children():
        img_display.destroy()

    subprocess.call(['./yolo3','detect','cfg/yolov3.cfg','yolov3.weights',image_data])
    image_data = 'predictions.jpg'
    basewidth = 800 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()

root = tk.Tk()
root.title('Asssessment 2: Mini Project')

root.iconbitmap('class.ico')
root.resizable(False, False)
title = tk.Label(root, text="Object Localization and Classificaiton using YOLOv3", padx=10, pady=20, font=("", 26)).pack()
canvas = tk.Canvas(root, height=500, width=1000, bg='white').pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=load_img)
chose_image.pack(side=tk.LEFT)

class_image = tk.Button(root, text='Classify Image',
                        padx=35, pady=10,
                        fg="white", bg="grey", command=classify)
class_image.pack(side=tk.RIGHT)
root.mainloop()
