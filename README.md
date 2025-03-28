# EX01 Developing a Simple Webserver
## Date:27.3.2025
## Name:Sathish kumar.T
## Reg no:212224100053

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
from http.server import HTTPServer,BaseHTTPRequestHandler
content="""" 
<!DOCTYPE html>
<html>
<head>
    <title>Simple Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr{
            background-color: aqua;
        }
    </style>
</head>
<body>
    <h2>TCP/IP Protocols</h2>
    <table>
        <tr>
            <th>S.no</th>
            <th>Layers</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Application Layer</td>
            <td>HTTP,FTP,Telnet,DNS</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Transport Layer</td>
            <td>TCP,UDP</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Internet Layer</td>
            <td>IPv4,IPv6</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Network Access Layer</td>
            <td>Ethernet,MAC</td>
        </tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

## OUTPUT:
![Screenshot 2025-03-27 234503](https://github.com/user-attachments/assets/7082e0f7-85ab-42eb-8866-538ab93149e1)

![Screenshot 2025-03-27 233904](https://github.com/user-attachments/assets/fca50fc7-b122-477c-b9cd-6c20014bd39f)



## RESULT:
The program for implementing simple webserver is executed successfully.
