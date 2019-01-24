from common import *

def handler(event, context):
    credentials = aws_SecretsManager()
    sql = sqlStatement(credentials, "SELECT * FROM logs ORDER BY time DESC")
    return packResponse(sql)
