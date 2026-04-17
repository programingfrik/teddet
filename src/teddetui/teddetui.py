#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import ttk
#import libteddet

class TeddetUI(#Frame
):
    def __init__(self, # master = None
                 ):
        # tki.Frame.__init__(self, master)

        # top = self
        self.root = tki.Tk()
        #top = tki.Toplevel(root)
        # win = self.master

        self.root.title("TEDDET")

        self.build_menu()

        # print(win.configure())
        # root = tki.Tk(className = "TeddetUI")
        # frm = ttk.Frame(root)
        # frm.grid()
        # self.menubar = tki.Menu(root)
        # self.top = top = tki.window.ListedTopLevel(root, menu = self.menubar)

        # print(f"root.winfo_name: " + root.winfo_name())
        # print(f"root.__class__: {root.__class__}")
        # print(f"dir(root): {dir(root)}")

        self.root.mainloop()

    def build_menu(self):
        self.root.option_add("*tearOff", False)

        self.menubar = tki.Menu(self.root)
        self.root["menu"] = self.menubar

        menu_file = tki.Menu(self.menubar)
        self.menubar.add_cascade(menu = menu_file, label = "File")
        menu_file.add_command(label = "New", command = self.com_new)
        menu_file.add_command(label = "Open", command = self.com_open)
        menu_file.add_command(label = "Reload", command = self.com_open)
        menu_file.add_command(label = "Save", command = self.com_save)
        menu_file.add_command(label = "Save As", command = self.com_save)

        menu_edit = tki.Menu(self.menubar)
        self.menubar.add_cascade(menu = menu_edit, label = "Edit")
        menu_edit.add_command(label = "Copy", command = self.com_copy)
        menu_edit.add_command(label = "Paste", command = self.com_paste)

        menu_form = tki.Menu(self.menubar)
        self.menubar.add_cascade(menu = menu_form, label = "Format")
        menu_form.add_command(label = "choose Format", command = self.com_choose_form)

        menu_help = tki.Menu(self.menubar)
        self.menubar.add_cascade(menu = menu_help, label = "Help")
        menu_help.add_command(label = "Manual", command = self.com_manual)
        menu_help.add_command(label = "About", command = self.com_about)

    def com_new(self):
        pass

    def com_open(self):
        pass

    def com_save(self):
        pass

    def com_copy(self):
        pass

    def com_paste(self):
        pass

    def com_choose_form(self):
        pass

    def com_manual(self):
        pass

    def com_about(self):
        pass


def main():
    app = TeddetUI()
    # app.mainloop()

if __name__ == "__main__":
    main()
