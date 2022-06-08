import cv2
import time
import numpy as np


class Video :

    def __init__(self, filename) :
        self.filename = filename
        self.load()


    def load (self) :
        video = cv2.VideoCapture(self.filename)

        if (video.isOpen() == False) :
            print ("Error opening video stream or file")

        while (video.isOpen()) :
            
            #Capture frame-by-frame
            ret, frame = video.read()

            if ret == True :

                #Display the resulting frame
                cv2.imshow('Video-App', frame)

                #wait until ant key is pressed
                if cv2.waitKey(25) and 0xFF == ord('p') :
                    cv2.waitKey(-1)

            else :
                break
    

    def exit (self) :
        video.realase()
        cv2.destroyAllWindows()

