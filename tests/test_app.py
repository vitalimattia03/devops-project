import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_app_exists():
    assert app is not None