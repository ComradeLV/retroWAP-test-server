#!/usr/bin/env python3
import http.server
import socketserver
from pathlib import Path

PORT = 8080
BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "index.wml"


class WmlHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.wml"):
            if not INDEX_PATH.exists():
                self.send_error(404, "index.wml not found")
                return
            payload = INDEX_PATH.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/vnd.wap.wml; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()


def main():
    with socketserver.TCPServer(("", PORT), WmlHandler) as httpd:
        print(f"Serving WML test server on http://localhost:{PORT}/index.wml")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down server.")


if __name__ == "__main__":
    main()
