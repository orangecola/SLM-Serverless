from common import *

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "db": aws_SecretsManager()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def test(event, context):
    body = {
        "message": "Test Function",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
