from common import *

def hello(event, context):
    credentials = aws_SecretsManager()
    sql = sqlStatement(credentials, "SELECT VERSION()")
    body = {
        "sql": sql,
        "db": credentials
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
