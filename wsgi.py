"""Module defining the WSGI callable function."""
from app import run_app

# Set the WSGI callable to the run function
application = run_app
