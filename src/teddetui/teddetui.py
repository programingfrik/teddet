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
        # top.master.title("teddetui")
        root = tki.Tk()
        #top = tki.Toplevel(root)

        root.option_add("*tearOff", False)

        # win = self.master
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
