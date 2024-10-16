"""The main entry point for the application."""
import os
import webbrowser
from dotenv import load_dotenv
from http.server import HTTPServer, BaseHTTPRequestHandler

# Load environment variables from .env file
load_dotenv()


def get_html_content():
    """Get the HTML content from the template."""
    # Get the BLOG_NAME environment variable, default to "My Blog"
    blog_name = os.getenv("BLOG_NAME", "My Blog")

    # Read the HTML template from file
    with open('template.html', 'r') as file:
        html_template = file.read()

    # Replace the placeholder with the actual blog name
    html_content = html_template.replace('{{ blog_name }}', blog_name)

    return html_content


class BlogHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handler to serve the page."""

    def do_GET(self):
        """Serve the HTML content."""
        html_content = get_html_content()
        # Send HTTP response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))


def run_development_server(
    server_class=HTTPServer, handler_class=BlogHTTPRequestHandler
):
    """Run the development server."""
    port = int(os.getenv("SERVER_PORT", 8000))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting development server on port {port}...")

    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()


def run_app(environ, start_response):
    """WSGI application callable for production."""
    # Prepare HTML content
    html_content = get_html_content()

    # WSGI response headers and body
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    return [html_content.encode('utf-8')]


if __name__ == "__main__":
    if os.getenv("ENVIRONMENT") == "Development":
        run_development_server()
