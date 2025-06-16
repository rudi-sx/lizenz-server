import os
import json
from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Liest alle Konfigurationswerte aus den Umgebungsvariablen
        response_data = {
            'valid_until': os.environ.get('LICENSE_VALID_UNTIL', '1970-01-01'),
            'server_time': datetime.utcnow().isoformat(),
            'latest_version': os.environ.get('LATEST_VERSION', '0.0.0'),
            'download_url': os.environ.get('DOWNLOAD_URL', '')
        }
        
        # Sendet alle Daten als JSON-Antwort
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return