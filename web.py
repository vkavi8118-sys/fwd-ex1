from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
from http.server import HTTPServer, BaseHTTPRequestHandler

# TCP/IP Protocol Presentation Content
content = """
from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content with TCP/IP table
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Model</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f7; }
        h1 { color: #2c3e50; text-align: center; }
        table {
            border-collapse: collapse;
            width: 70%;
            margin: 30px auto;
            font-size: 18px;
        }
        th, td {
            border: 1px solid #333;
            padding: 12px;
            text-align: center;
        }
        th { background-color: #3498db; color: white; }
        tr:nth-child(even) { background-color: #ecf0f1; }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Model</h1>
    <table>
        <tr>
            <th>Layer</th>
            <th>Functions</th>
            <th>Examples</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>Provides services for user applications</td>
            <td>HTTP, FTP, SMTP, DNS</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>Ensures data delivery (reliable/unreliable)</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>Logical addressing, ro

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler


