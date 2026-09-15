#!/usr/bin/env python3
"""Hello World with an INTENTIONAL reflected XSS for code-scanner testing.

CWE-79: user-controlled query parameter is written into HTML with no escaping.
Do not use this pattern in real software.
Repo update to trigger scanning
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        name = query.get("name", ["World"])[0]

        # INTENTIONAL XSS: unsanitized user input interpolated into HTML.
        html = f"<html><body><h1>Hello, {name}!</h1></body></html>"

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    print("Hello, World!")
    print("XSS demo server on http://127.0.0.1:8000/?name=World")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
