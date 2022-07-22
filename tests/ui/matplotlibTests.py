import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




from tkinter import *
root = Tk()
root.geometry("1000x200")
root.title("matplotlib test")  #

name = "matplotlib test for the tkinter insertion"
timer = np.array([0.0, 0.1, 0.2, 0.5, 0.6, 0.615, 0.7, 0.78, 0.8, 0.83, 1.01, 1.02, 1.03, 1.04, 2.05, 5, 6.2, 6.3, 6.5, 7.4, 7.6, 8, 9.2, 9.5, 9.6, 9.7, 9.9, 10, 10.2, 10.5, 10.6, 12.7, 12.8, 12.9, 13, 15, 15.5, 15.6, 15.8, 16, 18 , 18.5, 19,20])
values = np.array([1, 6, 5, 9, 3, 4, 33, 6 ,2, 1, 5, 8, 4, 5, 6, 2, 3, 9, 3, 2, 6, 9, 3, 5, 84, 65, 3, 9, 6, 5, 87, 9, 6, 5, 63, 52, 41, 85, 74, 96, 63, 56, 45, 78])

def plotAGraph () :
    axe_x = timer
    axe_y = values
    figure = plt.figure(figsize=(5, 4), dpi=100)
    figure.add_subplot(111).plot(axe_x, axe_y)
    #plt.plot(axe_x, axe_y)
    chart = FigureCanvasTkAgg(figure, root)
    chart.get_tk_widget().grid(row=5, column=0)

    plt.grid()


button = Button(root, text="Graph it !", command=plotAGraph)
button.grid()


root.mainloop()