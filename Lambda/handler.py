from common import *

def getLogs(event, context):
    credentials = aws_SecretsManager()
    sql = sqlStatement(credentials, "SELECT * FROM logs ORDER BY time DESC")
    return packResponse(sql)

def getModules(event, context):
    credentials = aws_SecretsManager()
    sql = sqlStatement(credentials, "SELECT * FROM modules")
    return packResponse(sql)
