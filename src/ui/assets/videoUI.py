from src.core import video as vd
from PIL import ImageTk, Image
import cv2

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


    
