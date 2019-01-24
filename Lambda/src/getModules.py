from common import *

def handler(event, context):
    credentials = aws_SecretsManager()
    sql = sqlStatement(credentials, "SELECT * FROM modules")
    return packResponse(sql)
