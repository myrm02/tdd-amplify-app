import json

users = [
    {"username": "admin@admin.com", "password": "admin"},
    {"username": "madeleine@la-maree.com", "password": "Madeleine67"}
]

def getUser(email: str):
  for user in users:
    if user['username'] == email:
        return user
    else :
       return {"error": "L'utilisateur n'existe pas !"}

def userHandler(event, context):
  print('received event:')
  print(event)

  body = getUser(event["body"]["email"])

  if body != {"error": "L'utilisateur n'existe pas !"}:
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
      'statusCode': 404,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps(body)
  }