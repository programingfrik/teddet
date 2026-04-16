#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import ttk
#import libteddet

class TeddetUI():
    def __init__(self, # master = None
                 ):
        # tki.Frame.__init__(self, master)

        # top = self
        root = tki.Tk()
        #top = tki.Toplevel(root)
        # win = self.master

        root.option_add("*tearOff", False)

        root.title("teddetui")

        menu_prin = tki.Menu(root)
        root["menu"] = menu_prin
        menu_file = tki.Menu(menu_prin)
        menu_prin.add_cascade(menu = menu_file, label = "File")

        # print(win.configure())
        # root = tki.Tk(className = "TeddetUI")
        # frm = ttk.Frame(root)
        # frm.grid()
        # self.menubar = tki.Menu(root)
        # self.top = top = tki.window.ListedTopLevel(root, menu = self.menubar)

        print(f"root.winfo_name: " + root.winfo_name())
        print(f"root.__class__: {root.__class__}")
        print(f"dir(root): {dir(root)}")
        root.mainloop()

def main():
    app = TeddetUI()
    # app.mainloop()

if __name__ == "__main__":
    main()
