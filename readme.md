### Network Infrastructure Demo

This repo is two things:
- a command-line interface that supports common shell commands
- ... and allows you create / manage instances of HTTP servers
- ... which you can view the source code for [here](https://github.com/dakota-byte/http-server)
- a simple client to simulate the requests a browser would make to DNS servers to fetch content

### The command-line shell

- Supports commands specific to getting my WWW demo set up
- Supports basic linux commands such as: ls, cd, pwd, mkdir, touch, echo, and more!
- Uses a default %PATH% of C:/WINDOWS/system32 to search for binaries
- Uses pssuspend.exe from Microsoft PSTools for SIGSTOP and SIGCONT behavior

### Custom Commands

- The following commands are available to manage an HTTP server:
    - http list
    - http create
    - http start
    - http stop
    - http resume

### Try it out

The following sequence of commands should paint an idea of what this is

`http create google 9998` # creates a server on port 9998 that can be tracked

`http create roblox 9999` # creates another server on port 9999

`http list` # lists the two servers, marked as [created]

`http start google` # begins running the HTTP server, take note of the PID printed!

`http list` # will now show google is [running]

`http set google 16828` # set PID of google to allow this program to manage it

`curl -v http://localhost:9998/` # will send a request, and you should recieve a 200 OK response

`http stop google` # if PID was set earlier, this stops google. listing will show [stopped] and any requests to Google will hang until resumed

`http resume google` # will resume the google server and response to any queued requests

`curl -v POST http://localhost:9998/files/homepage -H "Content-Length: 7" -H "Content-Type: application/octet-stream" -d 'GOOGLE!'` # this is up to the server host to create! imagine this is a beautiful HTML page

`http search google.com/homepage` # will show contents of homepage (like a browser search)