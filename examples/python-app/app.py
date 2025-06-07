"""
app.py

A simple HTTP server that responds with a JSON health check.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler that provides a JSON health endpoint.
    """

    def do_get(self):
        """
        Handle GET requests and return a JSON-formatted health status.
        """
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = {"status": "healthy", "service": "python-api"}
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
    print("Server started on port 8080")
    server.serve_forever()
