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
pyinterpath = None
inter = None

def com_execute(subject):
    global projectdir, cwdrel, pyinterpath, inter
    print(f"com_execute {subject}")
    path = ""
    args = []
    if subject == "teddetgui":
        os.chdir(projectdir.joinpath("src"))
        path = pyinterpath.joinpath(inter)
        args += [path, "-m", "teddetgui"]
    elif subject == "libteddet_tests":
        os.chdir(projectdir.joinpath("src", "libteddet_tests"))
        path = get_bin_path("haxe").joinpath("haxe")
        args = [path, "-main", "TestBasics", "--interp", "-L", "utest"]
    else:
        print(f"Error: don't know how to execute {subject}")
        return
    os.execv(path, args)

def com_build(subject):
    global projectdir, cwdrel
    print(f"com_build {subject}")
    if subject == "libteddet":
        os.chdir(projectdir)
        path = get_bin_path("haxe").joinpath("haxe")
        args = [path, pathlib.Path("src", "libteddet", "build.hxml")]
    else:
        print(f"Error: don't know how to build {subject}")
        return
    os.execv(path, args)

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

def get_bin_path(bin):
    return [pathlib.Path(p, bin) for p in os.get_exec_path()
            if pathlib.Path(p, bin).exists()][0].parent

def get_paths():
    global projectdir, cwdrel, pyinterpath, inter
    parts = pathlib.Path(os.getcwd()).parts
    projectdir = pathlib.Path(*parts[:parts.index("teddet") + 1])
    cwdrel = pathlib.Path(*parts[parts.index("teddet") + 1:])
    pyinterpath = pathlib.Path(sys.orig_argv[0]).parent
    inter = pathlib.Path(sys.orig_argv[0]).name
    if not pyinterpath.is_absolute():
        pyinterpath = get_bin_path(inter)

def main():
    get_paths()
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
