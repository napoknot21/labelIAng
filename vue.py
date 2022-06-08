from tkinter import *
from tkinter import filedialog
import os

def getFileName () :
    filename = filedialog.askopenfilename(
        initialdir="./",
        title="Select a Video",
        filetypes=(
            ("AVI videos", "*.avi"),
            ("all files", "*.*")
        )
    )
    return filename

def browseFiles () :
    filename = getFileName()
    #Change label contents
    label_file_explorer.configure(text="File opened: " + filename)

# Principal window
window = Tk()

# Set window title
window.title("Video-App")

#Set window background color
window.geometry("707x500")

#Set window background color
window.config(background = "white")

#Create a File Explorer Label
label_file_explorer = Label(
    window,
    text="File Explorer using Tkinter",
    width=100,
    height=4,
    fg="blue"
)

def sent () :
    return os.path(getFileName())

#Create a button for browse files
button_explorer = Button(
    window,
    text="Browse Files",
    command=browseFiles
)

button_accept = Button(
    window,
    text="Accept"
)

button_sent = Button(
    window,
    text="Sent",
    command=sent
)

#Create an exit button
button_exit = Button(
    window,
    text="Exit",
    command=exit
)

# grid method is chosen for placing all widgets at respective positions in a table
# like structure by specifying rows and columns
label_file_explorer.grid(column=1, row=1)
button_explorer.grid(column=1, row=2)
button_accept.grid(column=1, row=3)
button_sent.grid(column=1, row=4)
button_exit.grid(column=1, row=5)

#Let the window for any event
window.mainloop()


