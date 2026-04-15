#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tki
#import libteddet

class TeddetUI(tki.Frame):
    def __init__(self, master = None):
        tki.Frame.__init__(self, master)
        tki.ttk.Entry(master).grid()
        master.option_add("*tearOff", false)
        top = tki.Toplevel(master)
        menu_prin = tki.Menu(top)
        menu_file = tki.Menu(menu_prin)
        menu_prin.add_cascade(menu = menu_file, label = "File")

def main():
    app = TeddetUI()
    app.mainloop()

if __name__ == "__main__":
    main()
