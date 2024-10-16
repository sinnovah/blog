"""
Module defining the wsgi callable function.

Do not add any environment variables here because this file is included in
source control. Use .env instead.
"""
import importlib.util
import os
import sys

# Add the application's directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Dynamically load the app module (app.py)
module_name = 'app'
module_path = 'app.py'

spec = importlib.util.spec_from_file_location(module_name, module_path)
app_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = app_module
spec.loader.exec_module(app_module)

# Set the WSGI callable to the run_app function
application = app_module.run_app
