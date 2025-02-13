# Simple Python HTTP Server with PUT Support

import http.server
import socketserver

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        """Handle file upload via PUT request"""
        file_path = self.path[1:]  # Remove leading "/"
        file_length = int(self.headers['Content-Length'])

        with open(file_path, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))

        self.send_response(201, "Created")
        self.end_headers()

PORT = 4444  # Change to your preferred port
Handler = MyHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"[*] Serving HTTP on port {PORT} - Upload enabled!")
    httpd.serve_forever()
