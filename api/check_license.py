import os
import json
from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Diese Funktion wird bei jeder Anfrage an die Vercel-URL ausgeführt.
        """
        # 1. Das Ablaufdatum aus einer sicheren Umgebungsvariable auslesen.
        #    Falls die Variable nicht gesetzt ist, wird ein vergangenes Datum als Fallback genutzt.
        valid_until_str = os.environ.get('LICENSE_VALID_UNTIL', '1970-01-01')

        # 2. Die Daten als JSON-Objekt vorbereiten.
        response_data = {
            'valid_until': valid_until_str,
            'server_time': datetime.utcnow().isoformat() # Nützlich für Debugging
        }

        # 3. Den HTTP-Response senden.
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        
        return