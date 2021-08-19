#! /usr/bin/python3
import sys

sys.path.insert(0, '/var/www/webstore/')
from webstore.app import app as application

application.secret_key = 'supersecretkey'
