import json
import os
import boto3
import ast
import mysql.connector

def aws_SecretsManager():
    #Pulls the database details from SecretsManager
    secret_name = os.environ['secret_name']
    region_name = os.environ['region']

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
    )
    connection_details = ast.literal_eval(get_secret_value_response["SecretString"])
    return [connection_details["username"], connection_details["password"], connection_details["host"], connection_details["db"]]

def sqlStatement(credentials, statement, data=None):
    mydb = mysql.connector.connect(
        user=credentials[0],
        passwd=credentials[1],
        host=credentials[2],
        db=credentials[3]
    )

    mycursor = mydb.cursor(prepared=True)
    if data == None:
        mycursor.execute(statement)
    else:
        mycursor.execute(statement, data)
    return mycursor.fetchall()

def packResponse(result):
    body = {
        "result": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
