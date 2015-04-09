# Psuedocode:
# Choose a directory (top level directory will be recursed into)
# Choose which file types indicate the folder SHOUDLN'T be deleted.
#   If choose .mp3, any folder containing a *.mp3 will not be deleted.
# Select if prompt before deletion
# Recursively delete all folders that do not contain anything we want.

# ======== Select a directory:
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

import Tkinter, tkFileDialog

root = Tkinter.Tk()
dirname = tkFileDialog.askdirectory()
if len(dirname ) > 0:
    print "You chose %s" % dirname 

root.focus_force() # Allow window to be focused after tkFileDialog

L1 = Label(root, text="File Types")
L1.pack( side = LEFT)
E1 = Entry(root, bd =5)

E1.pack(side = RIGHT)
E1.focus_set()

root.mainloop()