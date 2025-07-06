import pytest
# import boto3
import uuid
# from moto import mock_dynamodb
# from boto3.dynamodb.conditions import Attr
import sys
import os
import json

sys.path.append(os.path.abspath("./amplify/backend/function/userHandler/src"))
import index as userPush

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

def test_registration_with_wrong_email():

    email = "madeleine"
    password = "Madeleine67"

    assert email.__contains__('@') is False
    assert email.__contains__('.fr') or email.__contains__('.com') is False

    user_infos = userPush.register(email, password)
    userId = str(uuid.uuid4)

    assert user_infos == {"error": "The email you entered is not valid"}
    assert userPush.userHandler(json.dumps({"email": email, "password": password}, indent=4)).status_code == 400

def test_registration_with_wrong_password():

    email = "madeleine@email.com"
    password = "Maree"

    assert len(password) < 8

    user_infos = userPush.register(email, password)
    userId = str(uuid.uuid4)

    assert user_infos == {"error": "Your password is lower than 8 characters"}
    assert userPush.userHandler(json.dumps({"email": email, "password": password}, indent=4)).status_code == 400

def test_registration_with_right_syntax():
    # Insertion de plusieurs items
    # items = [
    #     {'id': '1', 'nom': 'Pomme', 'description': 'Fruit rouge sucré'},
    #     {'id': '2', 'nom': 'Banane', 'description': 'Fruit jaune'},
    #     {'id': '3', 'nom': 'Cerise', 'description': 'Petit fruit rouge'}
    # ]

    # for item in items:
    #     dynamodb_table.put_item(Item=item)

    email = "madeleine@la-maree.com"
    password = "Madeleine67"

    assert email.__contains__('@') is True
    assert email.__contains__('.fr') or email.__contains__('.com') is True
    assert len(password) > 8

    user_infos = userPush.register(email, password)
    userId = str(uuid.uuid4)

    assert user_infos == {"email": "madeleine@la-maree.com", "password": "Madeleine67"}
    assert userPush.userHandler(json.dumps({"email": email, "password": password}, indent=4)).status_code == 200

    #Add user to the table
    # dynamodb_table.put_item(Item={
    #     'userId': userId, 
    #     'email': user_infos["email"],
    #     'password': user_infos["password"]
    # })

    # response = dynamodb_table.scan(
    #     FilterExpression=Attr('email').contains(user_infos["email"])
    # )

    # results = response['Items']

    # print(results)

    #assert results == {}