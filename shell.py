import subprocess
import sys

from simples import *
from HTTPServer import *

builtins = {
    "exit": handle_exit,
    "echo": handle_echo,
    "pwd": handle_pwd,
    "cd": handle_cd,
    "ls": handle_ls,
    "mkdir": handle_mkdir,
    "touch": handle_touch,
    "http": handle_http,
}


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, *args = input().split(" ")

        if command in builtins:
            builtins[command](args)
            continue
        elif executable := locate_executable(command):
            subprocess.run([executable, *args])
        else:
            print(f"{command}: command not found")

        sys.stdout.flush()


if __name__ == "__main__":
    main()
