"""
Module defining the wsgi callable function.

Do not add any environment variables here because this file is included in
source control. Use .env instead.
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

module_name = 'wsgi'
module_path = 'app.py'

spec = importlib.util.spec_from_file_location(module_name, module_path)
wsgi = importlib.util.module_from_spec(spec)
sys.modules[module_name] = wsgi
spec.loader.exec_module(wsgi)

application = wsgi.application
