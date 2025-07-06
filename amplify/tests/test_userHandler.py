import pytest
# import boto3
import uuid
# from moto import mock_dynamodb
# from boto3.dynamodb.conditions import Attr
import sys
import os

sys.path.append(os.path.abspath("./amplify/backend/function/userHandler/src"))
import index as userHandler

#TABLE_NAME = os.environ.get("", "UserTable")
# Connexion à DynamoDB mocké
# dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# @pytest.fixture
# @mock_dynamodb
# def dynamodb_table():
#     # Création de la table
#         table = dynamodb.create_table(
#         TableName='users-dev',
#         KeySchema=[{'AttributeName': 'userId', 'KeyType': 'HASH'}],
#         AttributeDefinitions=[{'AttributeName': 'userId', 'AttributeType': 'S'}],
#         # GlobalSecondaryIndexes=[
#         #     {
#         #         "IndexName": "email",
#         #         "KeySchema": [{"AttributeName": "email", "KeyType": "HASH"}],
#         #         "Projection": {"ProjectionType": "ALL"}
#         #         "ProvisionedThroughout": {"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
#         #     }
#         # ]
#         ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
#         )
#         table.meta.client.get_waiter('table_exists').wait(TableName='users-dev')

#         yield table  # Rend la table disponible pour les tests

def test_get_existed_user():

    email = "admin@admin.com"

    result = userHandler.getUser(email)

    assert result == {"username": "admin@admin.com", "password": "admin"}

def test_get_unexisted_user():

    email = "johndoe@notfound.com"

    result = userHandler.getUser(email)

    assert result == {"error": "L'utilisateur n'existe pas !"}

    # response = dynamodb_table.scan(
    #     FilterExpression=Attr('email').contains(user_infos["email"])
    # )

    # results = response['Items']

    # print(results)

    #assert results == {}