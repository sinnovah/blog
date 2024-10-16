"""
Module defining the  callable function.

Do not add any environment variables here because this file is included in
source control. Use .env instead.
"""
from app import run_app


# Set the WSGI callable to the run_app function
application = run_app
