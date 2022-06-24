import cv2
import numpy as np
import time as tm

class Video :

	def __init__(self, filename) :
		self.filepath = filename
		self.start()

	def start (self) :
		self.video = cv2.VideoCapture(self.filepath)

		if (self.video.isOpened()== False):
			print("Error opening video stream or file")
	
		while(self.video.isOpened()) :

			# Capture frame-by-frame
			ret, frame = self.video.read()

			if ret == True:
										
    	    			# Display the resulting frame
				cv2.imshow('Video-app',frame)  

				# Wait until any key is pressed
				if cv2.waitKey(25) & 0xFF == ord('p'):
					cv2.waitKey(-1)
	
			# Break the loop
			else:
				break

	
	def exit (self) :
		self.video.release()
		#out.release() 
		cv2.destroyAllWindows()

v = Video("MobEyeQ3.avi")
