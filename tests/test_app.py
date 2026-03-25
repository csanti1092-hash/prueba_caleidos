import json
from src.app import lambda_handler


def test_lambda_handler():
    response = lambda_handler({}, None)

    assert response["statusCode"] == 200

    body = json.loads(response["body"])
    assert body["message"] == "Hello World"
