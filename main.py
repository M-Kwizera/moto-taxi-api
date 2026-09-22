import json
from http.server import HTTPServer, BaseHTTPRequestHandler


rides = []


class MotoTaxiHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        # http://localhost:8080/rides
        if self.path == "rides":
            self._set_headers(200)
            self.wfile.write(json.dumps(rides).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Path ntabwo yabonetse!"}).encode("utf-8"))

    def run():
        server_address = ("", 4040)
        httpd = HTTPServer(server_address, MotoTaxiHandler)
        print(f"Moto Taxi ==> server running on port {server_address[1]}")
        httpd.serve_forever()




    if __name__ == "__main__":
        run

    
