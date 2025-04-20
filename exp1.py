from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
    <body style="background-color: #f0f8ff; font-family: Arial, sans-serif;">
        <h1 align="center" style="color: #2c3e50;">About the System</h1>
        <table border="1" cellpadding="5" align="center" style="border-collapse: collapse; background-color: #ffffff;">
            <tr style="background-color: #2980b9; color: white;">
                <th>SYSTEM CONFIGURATION</th>
                <th>DESCRIPTION</th>
            </tr>
            <tr>
                <td style="background-color: #ecf0f1;">Processor</td>
                <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
            </tr>
            <tr>
                <td style="background-color: #ecf0f1;">Primary Memory</td>
                <td>Ram-16GB</td>
            </tr>
            <tr>
                <td style="background-color: #ecf0f1;">Secondary Memory</td>
                <td>Rom-512GB</td>
            </tr>
            <tr>
                <td style="background-color: #ecf0f1;">O.S</td>
                <td>Windows 11</td>
            </tr>
        </table>
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