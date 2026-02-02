
import http.server
import ssl
import sys

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('0.0.0.0', PORT), handler)

# Load certificates
# Should be in the same directory
try:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"Serving securely on https://localhost:{PORT}")
    httpd.serve_forever()
except FileNotFoundError:
    print("Error: cert.pem or key.pem not found. Run generate_cert.py first.")
    sys.exit(1)
except Exception as e:
    print(f"Server error: {e}")
    sys.exit(1)
