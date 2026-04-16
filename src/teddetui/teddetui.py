#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import ttk
#import libteddet

class TeddetUI(tki.Frame):
    def __init__(self, master = None):
        tki.Frame.__init__(self, master)
        top = tki.Frame(master)
        top.master.title("teddetui")
        top.option_add("*tearOff", False)
        win = tki.Toplevel(top)
        menu_prin = tki.Menu(win)
        win["menu"] = menu_prin
        menu_file = tki.Menu(menu_prin)
        menu_prin.add_cascade(menu = menu_file, label = "File")

def main():
    app = TeddetUI()
    app.mainloop()

if __name__ == "__main__":
    main()
