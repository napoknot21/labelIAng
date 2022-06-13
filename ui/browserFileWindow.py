from tkinter import *
from tkinter import filedialog

class BrowserFileWindow :

  def __init__ (self) :
    self.filename_video = None
    self.filename_csv = None
    self.windowInit()


  def windowInit(self) :
    self.window = Tk()
    self.filename = None
    self.window.title("Video-app")
    self.window.geometry("707x500")
    self.window.config(background="white")
    self.loadLabelExplorerVideo()
    self.loadLabelExplorerCsv()
    #self.loadSpace()
    self.buttonsLoadVideo()
    self.buttonsLoadCsv()
    self.buttonPlace()
    self.window.mainloop()

	
  def loadLabelExplorerVideo (self) :
    self.label_file_explorer_video = Label(
        self.window,
        text="Select a video file",
        width=100,
        height=5,
        fg="blue"
    )


  def loadLabelExplorerCsv (self) :
    self.label_file_explorer_csv = Label(
        self.window,
        text="Select a csv file",
        width=100,
        height=5,
        fg="blue"
    )  


  def loadSpace (self) :
    self.label_space = Label(
        self.window,
        width=100,
        height= 3
    )


  def openFileNameVideo (self) :
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select a Video",
        filetypes=(
            	("AVI videos", "*.avi"),
		("mp4 videos", "*.mp4"),
            	("all files", "*.*")
        )
	  )
    self.filename_video = filename
    self.printLabelContentVideo()


  def openFileNameCsv (self) :
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select a Video",
        filetypes=(
            	("Csv files", "*.csv"),
		("Exel files", "*.xls"),
            	("all files", "*.*")
        )
	  )
    self.filename_csv = filename
    self.printLabelContentCsv()



  def buttonsLoadVideo (self) :
    self.buttons_video = []
    #Create an explorer file button
    button_explorer = Button(
        self.window,
        text="Browse Files",
        command=self.openFileNameVideo
    )
    self.buttons_video.append(button_explorer)


  def buttonsLoadCsv (self) :
    self.buttons_csv = []
    #Create an explorer file button
    button_explorer = Button(
        self.window,
        text="Browse Files",
        command=self.openFileNameCsv
    )
    self.buttons_csv.append(button_explorer)



  def printLabelContentVideo (self) :
    self.label_file_explorer_video.configure(text="Video selected: " + self.filename_video)


  def printLabelContentCsv (self) :
    self.label_file_explorer_csv.configure(text="File csv selected: " + self.filename_csv)


  def buttonPlace (self) :
    self.label_file_explorer_video.grid(column=1, row=1)

    self.label_space.grid(column=1, row=2)

    for i in range (len(self.buttons_video)) :
      self.buttons_video[i].grid(column=1, row=i+3)

    self.label_space.grid(column=1, row=len(self.buttons_video)+3+1)

    self.label_file_explorer_csv.grid(column=1, row=len(self.buttons_video)+3+2)

    for j in range (len(self.buttons_csv)) :
      self.buttons_csv[j].grid(column=1, row=len(self.buttons_csv)+5+1+j)

    #Create an exit button
    button_exit = Button(
        self.window,
        text="Exit",
        command=exit
    )
    button_exit.grid(column=1, row=len(self.buttons_csv)+6+1)
    #self.buttons.append(button_exit)

  ################## Getters and Setters ##################

  def getFileNameVideoPath (self) :
    return self.filename_video


  def getFileNameCsvPath (self) :
    return self.filename_csv


# Ancient verison
"""
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
      
      
                                                                                                  
# principal window
window = Tk()
  
# Set window title
window.title('App-video')
  
# Set window size
window.geometry("707x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()
"""
