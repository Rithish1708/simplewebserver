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