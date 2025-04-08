# EX01 Developing a Simple Webserver
## Date:08-04-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html>
    <head>
        <title>
            TCP Protocal Suite
        </title>
    </head>
    <body>
        <h1 >List of Protocals</h1>
        <ul>
            <li>HTTP</li>
            <li>FTP</li>
            <li>SNMP</li>
            <li>SMTP</li>
            <li>Telnet</li>
            <li>DNS</li>
        </ul>
        <h3><b>Name:</b>Rithish R</h3>
        <h3><b>Register No:</b>212224040278</h3>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot (1).png>)
![alt text](<Screenshot (2).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
