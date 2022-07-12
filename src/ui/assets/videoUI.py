from matplotlib import image
from src.core import video as vd
from PIL import ImageTk, Image
import cv2
import tkinter

class VideoUI :

    def __init__ (self, master, filevideo) :
        self.master = master
        self.filevideo = vd.Video(filevideo)
        self.cap = self.filevideo.getVideo()
        self.video_stream()


    def getTotalNumberFrames (self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))


    def video_stream (self) :
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor (
            frame,
            cv2.COLOR_BGR2RGBA
        )
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.master.imgtk = imgtk
        self.master.configure(image=imgtk)
        delay = int(150/ self.cap.get(cv2.CAP_PROP_FPS))
        self.master.after(delay, self.video_stream)


    


"""
filename = "C:/Users/cmartin-/Desktop/app-pycharm-edition/MobEyeQ3.avi"
cap = cv2.VideoCapture(filename)

if not cap.isOpened :
    print("Could not open " + filename)
    exit(1)

lenght = int (cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)


print(lenght)
print(width)
print(height)
print(fps)
"""