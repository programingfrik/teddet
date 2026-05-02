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
hxbin = None

def com_execute(subject):
    global projectdir, pyinterpath, inter, hxbin, cwdrel
    print(f"com_execute {subject}")
    cwd = projectdir.joinpath(cwdrel)
    initpath = None
    path = None
    args = []
    env = os.environ
    if subject == "teddetgui":
        initpath = projectdir.joinpath("src")
        env["PYTHONPATH"] = initpath
        path = pyinterpath.joinpath(inter)
        args = [path, "-m", "teddetgui"]
    elif subject == "libteddet_tests":
        initpath = projectdir.joinpath("src", "libteddet_tests").relative_to(cwd, walk_up = True)
        path = get_bin_path(hxbin).joinpath(hxbin)
        args = [path, "-p", initpath, "-main", "TestBasics", "--interp", "-L", "utest"]
    else:
        print(f"Error: don't know how to execute {subject}")
        return
    print(f"Initial path: {initpath}")
    print("Excuting: {0}".format(" ".join([str(a) for a in args])))
    os.execve(path, args, env)

def com_build(subject):
    global projectdir, hxbin, cwdrel
    print(f"com_build {subject}")
    cwd = projectdir.joinpath(cwdrel)
    initpath = None
    path = None
    args = []
    if subject == "libteddet":
        initpath = projectdir.joinpath("src").relative_to(cwd, walk_up = True)
        path = get_bin_path(hxbin).joinpath(hxbin)
        args = [path, "-p", initpath,
                projectdir.joinpath("src", "libteddet", "build.hxml").relative_to(cwd, walk_up = True)]
    else:
        print(f"Error: don't know how to build {subject}")
        return
    print(f"Initial path: {initpath}")
    print("Excuting: {0}".format(" ".join([str(a) for a in args])))
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
    global projectdir, cwdrel, pyinterpath, inter, hxbin
    parts = pathlib.Path(os.getcwd()).parts
    projectdir = pathlib.Path(*parts[:parts.index("teddet") + 1])
    cwdrel = pathlib.Path(*parts[parts.index("teddet") + 1:])
    pyinterpath = pathlib.Path(sys.orig_argv[0]).parent
    inter = pathlib.Path(sys.orig_argv[0]).name
    if not pyinterpath.is_absolute():
        pyinterpath = get_bin_path(inter)
    hxbin = "haxe.exe" if sys.platform == "win32" else "haxe"

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
        print(f"Error: {args.command} is not a valid command."
              + " Try \"execute\", \"build\" or \"pack\".")
    else:
        infere_action()

if __name__ == "__main__":
    main()
