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

def com_execute(subject):
    if subject == "teddetgui":
        print("Not implemented yet")
        print(os.getcwd())
    elif subject == "libteddet_tests":
        print("Not implemented yet")
    pass

def com_build(subject):
    if subject == "libteddet":
        print("Not implemented yet")

def com_pack():
    print("Not implemented yet")

def infere_action():
    print("infere_action")
    print("Not implemented yet")

def main():
    cliparser = argparse.ArgumentParser()
    cliparser.add_argument("command", help = "The command that yout want to execute", nargs = "?")
    cliparser.add_argument("subject", help = "This is the subject of the command", nargs = "?")
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
