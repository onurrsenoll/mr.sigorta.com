import sys
import os

# Uygulama dizinini Python path'e ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from a2wsgi import ASGIMiddleware
from main import app

# cPanel Phusion Passenger bu 'application' değişkenini kullanır
application = ASGIMiddleware(app)
