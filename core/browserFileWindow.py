from tkinter import *
from tkinter import filedialog

class BrowserFileWindow :

  def __init__ (self) :
    self.windowInit()
    self.openFileName()
    #self.printLabelContent()


  def windowInit(self) :
    self.window = Tk()
    self.window.title("Video-app")
    self.window.geometry("707x500")
    self.window.config(background="white")
    self.loadLabelExplorer()
    self.buttonsLoad()
    self.buttonPlace()
    self.window.mainloop()


  def openFileName (self) :
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select a Video",
        filetypes=(
            	("AVI videos", "*.avi"),
            	("all files", "*.*")
        )
	  )
    self.filename = filename


  def loadLabelExplorer (self) :
    self.label_file_explorer = Label(
        self.window,
        text="File Explorer using Tkinter",
        width=100,
        height=4,
        fg="blue"
    )


  def buttonsLoad (self) :
    self.buttons = []

    #Create an explorer file button
    button_explorer = Button(
        self.window,
        text="Browse Files",
        command=self.openFileName()
    )
    self.buttons.append(button_explorer)

    #Create a accpet button const
    button_accept = Button(
        self.window,
        text="Accept"
    )
    self.buttons.append(button_accept)

    #Create an exit button
    button_exit = Button(
        self.window,
        text="Exit",
        command=exit
    )
    self.buttons.append(button_exit)


  def printLabelContent (self) :
    self.label_file_explorer.configure(text="File opened: " + self.filename)


  def buttonPlace (self) :
    self.label_file_explorer.grid(column=1, row=1)
    for i in range (len(self.buttons)) :
      self.buttons[i].grid(column=1, row=i+2)


  ################## Getters and Setters ##################

  def getFilenamePath () :
    return self.filename



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
