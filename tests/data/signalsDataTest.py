"""import pandas as pd
import numpy as np

data = pd.read_csv("../../.data/import/savesSignals.csv")
name = data["File"]
print (data.columns.tolist())
print(name[0] if len(name[0]) != 0  else "None")
name[0] = "newfile.txt"
print(name[0] if len(name[0]) != 0  else "None")"""

from tkinter import *
from PIL import ImageTk, Image
import cv2

root = Tk()
root.title("Video app test")

app = Frame (root, bg="white")
app.grid()

lmain = Label (app, text="hello")
lmain.grid()

cap = cv2.VideoCapture("C:/Users/cmartin-/Downloads/app/MobEyeQ3.avi")

def video_stream () :
    _, frame = cap.read()
    cv2image = cv2.cvtColor (
        frame,
        cv2.COLOR_BGR2RGBA
    )
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    delay = int(140 / cap.get(cv2.CAP_PROP_FPS)) 
    lmain.after(delay, video_stream)

video_stream()
root.mainloop()


"""from tkinter import *
import imageio
from PIL import Image, ImageTk
def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return   
########### Main Program ############

root = Tk()
root.title('Video in a Frame')
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "C:/Users/cmartin-/Desktop/app-pycharm-edition/MobEyeQ3.avi"   #Image-path
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])
stream()
root.mainloop()"""