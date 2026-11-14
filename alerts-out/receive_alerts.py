"""Receive AIRlert alerts in your own system: a minimal HTTPS endpoint AIRlert LIVE can call.

Run it behind your own HTTPS (a reverse proxy or your gateway's web server). FP sets AIRlert LIVE to
call your address with the shared secret you agree; the fields are confirmed with you per project.
"""
import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SECRET = os.environ.get("AIRLERT_SHARED_SECRET", "change-me")


class AlertHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if not hmac.compare_digest(self.headers.get("X-Shared-Secret", ""), SECRET):
            self.send_response(403)
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", 0))
        alert = json.loads(self.rfile.read(length) or b"{}")
        # Example: {"hub": "HUB-0001", "sensor": "Bed 3", "alert": "convulsion", "time": "..."}
        print("AIRlert alert:", alert)
        # Hand it to your own system here: nurse call, pager, app, log.
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), AlertHandler).serve_forever()
