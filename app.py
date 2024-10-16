"""The main entry point for the application."""
import webbrowser
from configuration import Configuration
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import psycopg2  # type: ignore
from psycopg2 import OperationalError  # type: ignore


def get_html_content():
    """Get the HTML content from the template."""
    # Get the BLOG_NAME environment variable
    blog_name = Configuration.get_blog_name()

    # Read the HTML template from file
    with open('template.html', 'r') as file:
        html_template = file.read()

    # Replace the placeholder with the actual blog name
    html_content = html_template.replace('{{ blog_name }}', blog_name)

    return html_content


class BlogHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handler to serve the page."""

    def do_GET(self):
        """Serve the HTML content or public static assets."""
        if self.path.startswith(('/css/', '/js/', '/images/')):
            # Serve static files from /public directory
            self.serve_static_file(self.path)
        else:
            # Serve dynamic content (HTML)
            self.serve_html()

    def serve_html(self):
        """Serve the main HTML page."""
        html_content = get_html_content()
        # Send HTTP response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

    def serve_static_file(self, path):
        """Serve static files like CSS, JS, or images."""
        # Adjust file path relative to the public folder
        file_path = os.path.join('./public', path.lstrip('/'))

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                # Send appropriate content type based on file extension
                self.send_response(200)
                if file_path.endswith('.css'):
                    self.send_header("Content-type", "text/css")
                elif file_path.endswith('.js'):
                    self.send_header("Content-type", "application/javascript")
                elif file_path.endswith('.png'):
                    self.send_header("Content-type", "image/png")
                elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                    self.send_header("Content-type", "image/jpeg")
                elif file_path.endswith('.gif'):
                    self.send_header("Content-type", "image/gif")
                elif file_path.endswith('.svg'):
                    self.send_header("Content-type", "image/svg+xml")
                elif file_path.endswith('.io'):
                    self.send_header("Content-type", "image/x-icon")
                else:
                    self.send_header(
                        "Content-type", "application/octet-stream"
                    )
                self.end_headers()
                self.wfile.write(file.read())
        else:
            # File not found
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def check_database_connection():
    """Check the connection to the database."""
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host=Configuration.get_database_host(),
            database=Configuration.get_database_name(),
            user=Configuration.get_database_user(),
            password=Configuration.get_database_password(),
        )
        # If the connection is successful
        print("Connection to the database was successful.")
        return True
    except OperationalError as e:
        # Handle any connection errors
        print(f"Failed to connect to the database: {e}")
        return False
    finally:
        if 'connection' in locals():
            connection.close()  # Close the connection if it was established


def run_development_server(
    server_class=HTTPServer, handler_class=BlogHTTPRequestHandler
):
    """Run the development server."""
    # Check the database connection
    check_database_connection()
    port = Configuration.get_server_port()
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting development server on port {port}...")

    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()


def run_app(environ, start_response):
    """WSGI application callable for production."""
    # Check the database connection
    if not check_database_connection():
        # If the connection fails, return a 500 Internal Server Error
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b"Database connection failed. Please try again later."]

    # Prepare HTML content
    html_content = get_html_content()

    # WSGI response headers and body
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    return [html_content.encode('utf-8')]


if __name__ == "__main__":
    if Configuration.get_environment() == "Development":
        run_development_server()
