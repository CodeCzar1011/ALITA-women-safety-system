#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 3000

# Change to the public directory
os.chdir('/mnt/c/Users/Owner/Desktop/hackathon/WEB 2/women-safety-analytics/public')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Alita Rescue Wave Shield server running at http://localhost:{PORT}")
    print("📁 Serving from women-safety-analytics/public")
    print(f"🗺️ Map available at http://localhost:{PORT}/map.php")
    
    # Open browser
    webbrowser.open(f'http://localhost:{PORT}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped.")
