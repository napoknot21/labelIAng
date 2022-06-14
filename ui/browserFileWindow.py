from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class BrowserFileWindow :

  #Constructor
  def __init__ (self) :
    self.filename_video = None
    self.filename_csv = None
    self.windowInit()


  #Initialize the window properties
  def windowInit(self) :
    self.window = Tk()
    self.filename = None
    self.window.title("Video-app")
    self.window.geometry("707x500")
    self.window.eval('tk::PlaceWindow . center')
    self.window.config(background="white")
    self.loadLabelExplorerVideo()
    self.loadLabelExplorerCsv()
    self.loadLabelSubmitExit()
    self.loadSpace()
    self.buttonsLoadVideo()
    self.buttonsLoadCsv()
    self.buttonPlace()
    self.window.mainloop()


  #Label where the video path will be printed	
  def loadLabelExplorerVideo (self) :
    self.label_file_explorer_video = Label(
        self.window,
        text="Select a video file",
        width=100,
        height=5,
        fg="blue"
    )


  #Label where the video path will be printed
  def loadLabelExplorerCsv (self) :
    self.label_file_explorer_csv = Label(
        self.window,
        text="Select a csv file",
        width=100,
        height=5,
        fg="blue"
    )


  def loadLabelSubmitExit (self) :
    self.label_submit_exit = Label(
      self.window,
	    width=100,
      height=5,
      fg="blue"
    ) 


  #Label for creating a "space" between the explorer labels
  def loadSpace (self) :
    self.label_space = Label(
      self.window,
	    text="error",
      width=100,
	    fg="white",
      height= 3
    )


  #Window browser for the video file
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
    if len(self.filename_video) != 0 :
      self.printLabelContentVideo()


  #Window browser for the csv file
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
    if len(self.filename_csv) != 0:
      self.printLabelContentCsv()


  # Buttoms for the video label (canvas)
  def buttonsLoadVideo (self) :
    self.buttons_video = []
    #Create an explorer file button
    button_explorer = Button(
        self.window,
        text="Browse Files",
        command=self.openFileNameVideo
    )
    self.buttons_video.append(button_explorer)


  #Buttoms for the video label (canvas)
  def buttonsLoadCsv (self) :
    self.buttons_csv = []
    #Create an explorer file button
    button_explorer = Button(
        self.window,
        text="Browse Files",
        command=self.openFileNameCsv
    )
    self.buttons_csv.append(button_explorer)


  #Modify the Video canvas with the video path
  def printLabelContentVideo (self) :
    self.label_file_explorer_video.configure(text="Video selected: " + self.filename_video)


  #Modify the csv canvas with the csv path
  def printLabelContentCsv (self) :
    self.label_file_explorer_csv.configure(text="File csv selected: " + self.filename_csv)


  #Place all buttoms from video and csv in the window
  def buttonPlace (self) :
    self.label_file_explorer_video.grid(column=1, row=1) #1
    #self.label_space.grid(column=1, row=2) # row=2
    for i in range (len(self.buttons_video)) :
      self.buttons_video[i].grid(column=1, row=i+3) #i = 0 => row=3  
    #self.label_space.grid(column=1, row=len(self.buttons_video)+3)  # len = 1 + 3=> row=
    self.label_file_explorer_csv.grid(column=1, row=len(self.buttons_video)+3+1)  #len = 1 + 3 + 1 => row=5
    for j in range (len(self.buttons_csv)) :
      self.buttons_csv[j].grid(column=1, row=len(self.buttons_csv)+5+j) #len = 1 + 5 => row=6
    self.label_submit_exit.grid(column=1, row=len(self.buttons_csv)+5+1)

    #Create an exit button
    button_exit = Button(
        self.window,
        text="Exit",
        command=exit
    )

    #create an accept button
    button_accept = Button(
        self.window,
        text="Accept",
        command=self.destroyAndSend
    )

    button_accept.grid(column=1, row=len(self.buttons_csv)+6)
    self.label_submit_exit.grid(column=1, row=len(self.buttons_csv)+6+1)	
    button_exit.grid(column=1, row=len(self.buttons_csv)+6+1) #len = 1 + 6 => row=7

 
  def destroyAndSend (self) : 
    if (self.filename_video is None or self.filename_csv is None) or (len(self.filename_csv) == 0 or len(self.filename_video) == 0) :
      messagebox.showerror("Alert Message", message="You need to enter two files !")
      return
    self.window.destroy()


  ################## Getters and Setters ##################

  def getFileNameVideoAndCsvPath (self) :
    return self.filename_video, self.filename_csv
