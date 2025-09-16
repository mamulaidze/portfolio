#!/usr/bin/env python3
"""
Simple HTTP server for portfolio development
Run with: python serve.py
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

# Configuration
PORT = 8000
DIRECTORY = "public"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Enable CORS for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def open_browser():
    """Open browser after a short delay"""
    webbrowser.open(f'http://localhost:{PORT}')

def main():
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Portfolio server running at http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.path.abspath(DIRECTORY)}")
        print("🔥 Press Ctrl+C to stop the server")
        
        # Open browser after 1 second
        Timer(1.0, open_browser).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✨ Server stopped. Thanks for using the portfolio server!")

if __name__ == "__main__":
    main()