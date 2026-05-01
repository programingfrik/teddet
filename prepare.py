#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This is a simple python script to help me while building teddet. This script must work with python3 standard and work regardless of the OS or FileSystem or the location from it was called.
#
# This script can take this sub-commands and act accordingly:
# - execute teddetgui
# - execute libtedddet_tests
# - build libteddet
# - pack

# execute teddetgui
# "cd d:\\pmercader\\proyectos\\teddet\\src && \"c:\\Program Files\\Python314\\python.exe\" -m teddetgui"

# execute libteddet_tests
# haxe -main TestBasics --interp -L utest

# quiero saber la ruta de prepare.py para poder ejecutar las acciones
# 

import sys
import argparse
import os
import pathlib

projectdir = None
cwdrel = None

def com_execute(subject):
    global projectdir, cwdrel

    command = ""
    args = []
    
    if subject == "teddetgui":
        command = "cd d:\\pmercader\\proyectos\\teddet\\src && \"c:\\Program Files\\Python314\\python.exe\" -m teddetgui"
        args = []
    elif subject == "libteddet_tests":
        command = "haxe -main TestBasics --interp -L utest"
        args = []
    else:
        print(f"Error: {subject} is unknown")
        return

    os.execv()

def com_build(subject):
    global projectdir, cwdrel
    if subject == "libteddet":
        command = ""
        args = []
        print("Not implemented yet")
    else:
        print(f"Error: don't know how to build {subject}")

def com_pack():
    print("Not implemented yet")

def infere_action():
    global projectdir, cwdrel
    print("infere_action")
    if cwdrel.is_relative_to(pathlib.Path("src", "libteddet")):
        com_build("libteddet")
    elif cwdrel.is_relative_to(pathlib.Path("src", "libteddet_tests")):
        com_execute("libteddet_tests")
    else:
        com_execute("teddetgui")

def get_projectdir():
    global projectdir, cwdrel
    parts = pathlib.Path(os.getcwd()).parts
    projectdir = pathlib.Path(*parts[:parts.index("teddet") + 1])
    cwdrel = pathlib.Path(*parts[parts.index("teddet") + 1:])

def main():
    get_projectdir()
    cliparser = argparse.ArgumentParser()
    cliparser.add_argument("command", help = "Sub-command that yout want to execute", nargs = "?")
    cliparser.add_argument("subject", help = "Subject of the command", nargs = "?")
    args = cliparser.parse_args()
    
    if (args.command in ["execute", "build"]) and (not args.subject):
        cliparser.print_help()
        print(f"Error: {args.command} requires a subject.")
    elif (args.command == "execute") and (args.subject):
        com_execute(args.subject)
    elif (args.command == "build") and (args.subject):
        com_build(args.subject)
    elif args.command == "pack":
        com_pack()
    elif args.command:
        cliparser.print_help()
        print(f"Error: {args.command} is not a valid command.")
    else:
        infere_action()

if __name__ == "__main__":
    main()
