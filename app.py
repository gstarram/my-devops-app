from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 5000

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>DevOps CI/CD Automated Pipeline is Live!</h1>")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"Server starting on port {PORT}...")
    server.serve_forever()
