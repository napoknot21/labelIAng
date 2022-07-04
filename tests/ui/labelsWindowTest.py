"""import os, sys
from tkinter import *

userin = ""

root = Tk()
root.geometry('1080x660')
root.title('Terminal')
root.configure(bg="black")

e = Entry(root, textvariable=userin, fg='lime', bg='black')
e.grid()

def process (event=None) :
    content = e.get()
    print(content)

e.bind('<Return>', process)
root.mainloop()"""
"""
import tkinter as tk
import sys

def focus_out_event(event):
    print >> sys.stderr, "Focus-Out   event called with args: %s"%event
    print >> sys.stderr, "Entry Widget Content:               %s"%event.widget.get()
def key_release_event(event):
    print >> sys.stderr, "Key-Release event called with args: %s"%event
    print >> sys.stderr, "Entry Widget Content:               %s"%event.widget.get()

if __name__ == "__main__":
    root = tk.Tk()
    entry1 = tk.Entry(root)
    entry1.bind("", key_release_event)
    entry1.bind("", focus_out_event)
    entry1.grid()

    entry2 = tk.Entry(root)
    entry2.bind("", key_release_event)
    entry2.bind("", focus_out_event)
    entry2.grid()

    root.mainloop()"""

"""import tkinter as tk


class EntryBox:
    def __init__(self, value, option, section, grid_row, master_e):
        self.section = section
        self.option = option
        self.box = tk.Entry(master_e)
        self.box.grid(column=0, row=grid_row)
        self.serial_no = grid_row
        self.box.insert(0, value)
        self.box.bind("<Key>", lambda event: self.update_cfg(event, self, self.get_value()))

    def get_value(self):
        return self.box.get()


    def update_cfg(evt, entry_box,new_value):
        global config_file
        config_file.set(entry_box.section, entry_box.option, new_value)
        print ("Config file modified. "+entry_box.section+" "+entry_box.option+" "+new_value)

EntryBox(1, "option", "section", tk.Tk(),5 )"""


tab = ["obkect1", "objec2", "objec3", "objec4", "objec5"]

current_len = len (tab)

def add (tab):
    object_i = "Object6"
    tab.append (object_i)

def delete (pos, tab):
    if len(tab) == 0:
        return
    if len(tab) <= pos:
        return
    tab[pos] = None
    

def cleanTab(tab) :
    cmpt = 0
    for i in range (len(tab)):
        if tab[i] == None:
            cmpt += 1
    if cmpt == 0: return tab
    newTab = []
    for i in range(len(tab)):
        if tab[i] != None:
            newTab.append (tab[i])
    tab = newTab
    return tab


add(tab)
print(tab)
delete(2, tab)
delete(5, tab)
delete(1, tab)
print(tab)
tab = cleanTab(tab)
print(tab)
add(tab)
print(tab)
tab = cleanTab(tab)
print(tab)
mot = "0123456789"
for i in range(len(mot)):
    print(ord(mot[i]))


    
#print(hashmap)
