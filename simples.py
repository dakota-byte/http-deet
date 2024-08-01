import os
import sys

## IMPLEMENTATION OF SIMPLE BUILT IN COMMANDS
## IMPLEMENTATION OF SIMPLE BUILT IN COMMANDS
## IMPLEMENTATION OF SIMPLE BUILT IN COMMANDS


def handle_exit(args):
    sys.exit(int(args[0]) if args else 0)


def handle_echo(args):
    if not args:
        return
    print(" ".join(args))


def handle_pwd(args):
    print(f"{os.getcwd()}")


def handle_cd(args):
    if not args:
        print(f"cd: No directory specified")
        return
    path = "".join(args)
    path = os.path.expanduser(path)  # cheat :(
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")


def handle_ls(args):
    with os.scandir(".") as entries:
        for entry in entries:
            print(entry.name)


def handle_mkdir(args):
    if not args:
        print(f"mkdir: Directory name not specified")
        return
    path = "".join(args)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully")
    except OSError as error:
        print(f"Error creating directory '{path}': {error}")


def handle_touch(args):
    if not args:
        print(f"touch: File name not specified")
        return
    filename = "".join(args)
    try:
        with open(filename, "w"):
            pass
        print(f"File '{filename}' created successfully")
    except IOError as e:
        print(f"Unable to create file '{filename}': {e}")


def locate_executable(command):
    # PATH = os.environ["PATH"]
    PATH = "C:\\WINDOWS\\system32"
    file_path = os.path.join(PATH, command)
    file_path_exe = os.path.join(PATH, command + ".exe")
    if (os.path.isfile(file_path) or os.path.isfile(file_path_exe)) and (
        os.access(file_path, os.X_OK) or os.access(file_path_exe, os.X_OK)
    ):
        return file_path
