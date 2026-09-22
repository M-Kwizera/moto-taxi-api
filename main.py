import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class MotoTaxiHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    