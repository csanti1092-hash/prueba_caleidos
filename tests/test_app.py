import json
import sys
import os

# 👇 AGREGA ESTO: Agregar el root al path ANTES del import
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# 👇 CAMBIA ESTE IMPORT por uno directo:
from src.app import lambda_handler


def test_lambda_handler():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["message"] == "Hello World"
