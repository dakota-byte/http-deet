import os
import re
import subprocess


http_servers = []


class HTTPServer:
    def __init__(self, status, name, port, directory):
        self.status = status
        self.name = name
        self.port = port
        self.directory = directory
        self.process = None
        self.pid = None

    def __str__(self):
        
        msg = f"[PID: {self.pid}] [{self.status}] {self.name} on port {self.port} in {self.directory}"
        return msg
    
    def getName(self):
        return self.name

def handle_http(args):
    subcommand, *args = args
    subcommand = subcommand.lower()

    if subcommand == "list":
        for serv in http_servers:
            print(serv)

    if subcommand == "create":
        if len(args) < 2:
            print("Usage: http create NAME PORT [directory]")
            return

        if not args[1].isdigit():
            print("Port must be a number.")
            return

        directory = None
        if len(args) == 3:
            directory = args[2]
        else:
            directory = "./http-" + args[0]

        if len(args) > 3:
            print("Too many arguments.")
            return

        name = args[0]
        port = int(args[1])
        server_obj = HTTPServer("created", name, port, directory)
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory {directory}. Server ready to start.")
        except OSError as error:
            print(f"Error creating directory '{directory}': {error}")
        http_servers.append(server_obj)

    if subcommand == "start":
        if len(args) < 1:
            print("Usage: http start NAME")
            return
        server = None
        for serv in http_servers:
            if serv.name == args[0]:
                server = serv
        if not server:
            print(f"You need to create the server first. use [http create]")
            return

        if server.process:
            print(f"Server already started. Please use 'http resume PID'")
            return
        else:
            process = subprocess.Popen(
                [
                    "server.exe",
                    "--directory",
                    f"{server.directory}/",
                    "--port",
                    f"{server.port}",
                ]
            )

            server.process = process

        server.status = "running"

    if subcommand == "resume":
        if len(args) < 1:
            print("Usage: http resume NAME")
            return
        
        server = None
        for serv in http_servers:
            if serv.name == args[0]:
                server = serv
        if not server:
            print(f"This server does not exist. use [http list] to see whats running")
            return
        if not server.pid:
            print(f"This server does not have its PID set. use [http set] to set it")
            return
        
        subprocess.Popen(["pssuspend.exe", "-r", str(server.pid)])
        server.status = "running"

    if subcommand == "stop":
        if len(args) < 1:
            print("Usage: http stop NAME")
            return
        
        server = None
        for serv in http_servers:
            if serv.name == args[0]:
                server = serv
        if not server:
            print(f"This server does not exist. use [http list] to see whats running")
            return
        if not server.pid:
            print(f"This server does not have its PID set. use [http set] to set it")
            return
        
        subprocess.Popen(["pssuspend.exe", str(server.pid)])
        server.status = "stopped"

    if subcommand == "set":
        if len(args) < 1:
            print("Usage: http set NAME PID")
            return
        
        server = None
        for serv in http_servers:
            if serv.name == args[0]:
                server = serv
        if not server:
            print(f"This server does not exist. use [http list] to see whats running")
            return
        
        server.pid = int(args[1])

    if subcommand == "search":
        if len(args) < 1:
            print("Usage: http search URL")
            return
        URL = args[0]

        server_n, resource = URL.split(".com/") # just for showcasing :( be nice

        server = None
        for serv in http_servers:
            if serv.name == server_n:
                server = serv
        if not server:
            print(f"This server does not exist. use [http list] to see whats running")
            return

        # make the curl request
        subprocess.Popen(["curl", "-i", "http://localhost:"+str(server.port)+"/files/"+resource])