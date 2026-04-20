#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import ttk
from tkinter import messagebox
#import libteddet

class TeddetGUI():

    def __init__(self):
        self.root = tki.Tk()
        self.root.title("TEDDET")
        self.build_menu()
        self.root.mainloop()

    def build_menu(self):
        self.root.option_add("*tearOff", False)

        self.menub = tki.Menu(self.root)
        self.root["menu"] = self.menub

        menu_file = tki.Menu(self.menub)
        self.menub.add_cascade(menu = menu_file, label = "File")
        menu_file.add_command(label = "New", command = self.com_new)
        menu_file.add_command(label = "Open", command = self.com_open)
        menu_file.add_command(label = "Reload", command = self.com_open)
        menu_file.add_command(label = "Save", command = self.com_save)
        menu_file.add_command(label = "Save As", command = self.com_save)
        menu_edit = tki.Menu(self.menub)
        self.menub.add_cascade(menu = menu_edit, label = "Edit")
        menu_edit.add_command(label = "Copy", command = self.com_copy)
        menu_edit.add_command(label = "Paste", command = self.com_paste)
        menu_frmt = tki.Menu(self.menub)
        self.menub.add_cascade(menu = menu_frmt, label = "Format")
        menu_frmt.add_command(label = "Choose Format", command = self.com_choose_form)
        menu_frmt.add_command(label = "Format details", command = self.com_format_details)
        menu_help = tki.Menu(self.menub)
        self.menub.add_cascade(menu = menu_help, label = "Help")
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

    def com_format_details(self):
        pass

    def com_manual(self):
        pass

    def com_about(self):
        messagebox.showinfo(message = "Un pollo cruzó la calle", title = "Algo pasó", icon = messagebox.INFO)
        pass



def main():
    app = TeddetGUI()

if __name__ == "__main__":
    main()
