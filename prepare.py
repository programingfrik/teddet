#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This is a simple python script to help me while building
# teddet. This script must work with python3 standard and work
# regardless of the OS or FileSystem or the location from wich
# it was called.

# This script can take this sub-commands and act accordingly:
# - execute teddetgui
# - execute libtedddet_tests
# - build libteddet
# - pack

# The script tries to execute the commands using relative paths to the
# current directory from wich it was called so that any posible error
# that happens has a relative path for emacs to find.

# Emacs is responsible for determining the path to this script and put
# it in the compile-command variable.

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
        env["PYTHONPATH"] = str(initpath)
        path = pyinterpath.joinpath(inter)
        args = [path.name, "-m", "teddetgui"]
    elif subject == "libteddet_tests":
        initpath = projectdir.joinpath("src").relative_to(cwd, walk_up = True)
        path = get_bin_path(hxbin).joinpath(hxbin)
        hxmlp = projectdir.joinpath("src", "libteddet_tests", "run_tests.hxml").relative_to(cwd, walk_up = True)
        args = [path.name, "-p", initpath, hxmlp]
    else:
        print(f"Error: don't know how to execute {subject}")
        return
    print(f"Initial path: {initpath}")
    print(f"args: {args}")
    print("Excuting: {0}".format(" ".join([str(a) for a in args])))
    print("python d:\\pmercader\\proyectos\\teddet\\prepare.py")
    os.spawnve(os.P_WAIT, path, args, env)

def com_build(subject):
    global projectdir, hxbin, cwdrel
    print(f"com_build {subject}")
    cwd = projectdir.joinpath(cwdrel)
    initpath = None
    path = None
    argsl = []
    if subject == "libteddet":
        initpath = projectdir.joinpath("src").relative_to(cwd, walk_up = True)
        path = get_bin_path(hxbin).joinpath(hxbin)
        hxmlp = projectdir.joinpath("src", "libteddet", "build.hxml") \
                         .relative_to(cwd, walk_up = True)
        pyvp = projectdir.joinpath("build", "pyver", "libteddet.py") \
                        .relative_to(cwd, walk_up = True)
        csvp = projectdir.joinpath("build", "csver", "libteddet") \
                        .relative_to(cwd, walk_up = True)
        argsl = [[path.name, "-p", initpath, hxmlp]]
        argsl.append(argsl[0].copy())
        argsl[0] += ["--python", pyvp]
        argsl[1] += ["--cs", csvp]
    else:
        print(f"Error: don't know how to build {subject}")
        return
    print(f"Initial path: {initpath}")
    for args in argsl:
        print("Excuting: {0}".format(" ".join([str(a) for a in args])))
        os.spawnv(os.P_WAIT, path, args)

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
    if "teddet" not in parts:
        print("Error: Your away from the project dir,"
              + " get back in there and then call me again.")
        sys.exit(1)
    projectdir = pathlib.Path(*parts[:parts.index("teddet") + 1])
    cwdrel = pathlib.Path(*parts[parts.index("teddet") + 1:])
    pyinterpath = pathlib.Path(sys.executable).parent
    inter = pathlib.Path(sys.executable).name
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
