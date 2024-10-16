"""The main entry point for the application."""
import os
import webbrowser
from dotenv import load_dotenv
from http.server import HTTPServer, BaseHTTPRequestHandler

# Load environment variables from .env file
load_dotenv()


class BlogHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handler to serve the page."""

    def do_GET(self):
        """Serve the HTML content."""
        # Get the BLOG_NAME environment variable, default to "My Blog"
        blog_name = os.getenv("BLOG_NAME", "My Blog")

        # Read the HTML template from file
        with open('template.html', 'r') as file:
            html_template = file.read()

        # Replace the placeholder with the actual blog name
        html_content = html_template.replace('{{ blog_name }}', blog_name)

        # Send HTTP response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))


def run_development_server(
    server_class=HTTPServer,
    handler_class=BlogHTTPRequestHandler
):
    """Run the server indefinitely."""
    # Port number from the environment variable, or default to 8000
    port = int(os.getenv("SERVER_PORT", 8000))

    # '' means all available interfaces
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")

    # Open the browser automatically
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()


def run_app():
    """
    Run the application.

    This method need to stay here so that wsgi
    has something to call in production.
    """
    if os.getenv("ENVIRONMENT") == "Development":
        run_development_server()


if __name__ == "__main__":
    run_app()
