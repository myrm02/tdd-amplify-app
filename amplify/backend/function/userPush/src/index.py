import json
import sys
import os

users = [
    {"email": "admin@admin.com", "password": "admin"}
]

def register(email: str, password: str):
    
    if email == "" or "@" not in email:
      return {"error": "The email you entered is not valid"}
    elif len(password) <= 8:
      return {"error": "Your password is lower than 8 characters"}
    else:
      newUser = {"email": email, "password": password}
      users.append(newUser)
      return newUser

def userHandler(event, context):
  print('received event:')
  print(event)

  body = register(event["body"]["email"], event["body"]["password"])

  if body == {"email": event["body"]["email"], "password": event["body"]["password"]}:
     return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps(body)
    }
  else:
    return {
      'statusCode': 400,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps(body) 
    }