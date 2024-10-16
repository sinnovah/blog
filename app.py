"""The main entry point for the application."""
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Run the server indefinitely."""
    # Port number from the environment variable, or default to 8000
    port = int(os.getenv("SERVER_PORT", 8000))
    server_address = ('', port)  # '' means all available interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
