"""
File: FolderCleaner.py
Author: Dillon Beck

Classes:
    FileTypeWindow: Window that lets user enter file types.

"""
# Psuedocode:
# Choose a directory (top level directory will be recursed into)
# Choose which file types indicate the folder SHOUDLN'T be deleted.
#   If choose .mp3, any folder containing a *.mp3 will not be deleted.
# Select if prompt before deletion
# Recursively delete all folders that do not contain anything we want.


from Tkinter import Entry, Label, Button, LEFT, RIGHT
import Tkinter, tkFileDialog


def main():
    """Main method.
    """
    root = Tkinter.Tk()

    # Select a directory:
    dirname = tkFileDialog.askdirectory()
    if len(dirname) > 0:
        print "You chose %s" % dirname

    root.focus_force() # Allow window to be focused after tkFileDialog

    FileTypeWindow(root, dirname)

    root.mainloop()


class FileTypeWindow(object):
    """Window that lets user type in file types and begin processing.
    """

    BUTTON_FILE_TYPE = 1

    def __init__(self, parent, directory):
        self.parent = parent
        self.directory = directory

        self.label1 = Label(self.parent, text="File Types")
        self.label1.pack(side=LEFT)

        self.entry1 = Entry(self.parent, bd=5)
        self.entry1.pack(side=RIGHT)
        self.entry1.focus_set()

        self.button_file_type = Button(self.parent,
                                       text="Go!",
                                       command=lambda:
                                       self.on_button_clicked(
                                           self.BUTTON_FILE_TYPE))
        self.button_file_type.pack(side=RIGHT)


    def on_button_clicked(self, button_id):
        """Callback for when any button is clicked.

        Args:
            button_id: An identifier for the button.
        """

        if button_id == self.BUTTON_FILE_TYPE:
            self.button_file_type_clicked()

    def button_file_type_clicked(self):
        """Recursively remove folders not containing one of the chosen file types.

        """
        entry = self.entry1

        file_types = entry.get()
        self.parent.destroy()
        process(file_types, self.directory)



def process(file_types, directory):
    """Delete all folders inside a directory not containing some file types.

    Args:
        file_types: List of file types indicating a folder shouldn't be deleted.
            A single file type should only have the extension, no dot or
            wildcard character required.
            List Format:
                [mp3, avi, jpg]

        directory: Full path to the desired directory as a string.
            Example:
                C:/Users/Name/Documents

    """
    types = file_types.split(',')
    #TODO: Do deletion of empty directories.
    print types

    print directory


if __name__ == "__main__":
    main()
