from src.core import video as vd
import cv2
import tkinter

class VideoUI :

    def __init__ (self, master, filevideo) :
        self.master = master
        self.filevideo = vd.Video(filevideo)


    def getTotalNumberFrames (self):
        cap = self.filevideo.getVideo()
        return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


    


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