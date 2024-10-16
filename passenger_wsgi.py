"""
Module defining the wsgi callable function.

Do not add any environment variables here because this file is included in
source control. Use .env instead.
"""
from app import run_app
import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'app.py')
application = run_app
