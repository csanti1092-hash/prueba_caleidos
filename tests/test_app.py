# tests/test_app.py
import json
import sys
import os

# Asegurar que el root del proyecto está en el path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.app import lambda_handler


def test_lambda_handler():
    """Prueba básica del endpoint /hello"""
    event = {"httpMethod": "GET", "path": "/hello"}
    context = None
    
    response = lambda_handler(event, context)
    
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["message"] == "Hello World"
