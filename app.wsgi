#! /usr/bin/python3
import sys
import logging

logging.basicConfig(strea=sys.stderr)
sys.path.insert(0, '/var/www/webstore/')
from webstore.app import app as application

application.secret_key = 'supersecretkey'
