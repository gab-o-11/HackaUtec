import boto3
import hashlib
import uuid
import json
from datetime import datetime, timedelta

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def lambda_handler(event, context):
    # Entrada
    user_id = event.get('user_id')
    password = event.get('password')

    if not user_id or not password:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Faltan user_id o password'})
        }

    dynamodb = boto3.resource('dynamodb')
    usuarios_table = dynamodb.Table('t_usuarios')
    response = usuarios_table.get_item(Key={'user_id': user_id})

    if 'Item' not in response:
        return {
            'statusCode': 403,
            'body': json.dumps({'error': 'Usuario no existe'})
        }

    hashed_password_bd = response['Item']['password']
    hashed_password_input = hash_password(password)

    if hashed_password_input != hashed_password_bd:
        return {
            'statusCode': 403,
            'body': json.dumps({'error': 'Password incorrecto'})
        }

    # Generar token
    token = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(minutes=60)

    tokens_table = dynamodb.Table('t_tokens_acceso')
    tokens_table.put_item(Item={
        'token': token,
        'user_id': user_id,
        'expires': expires_at.strftime('%Y-%m-%d %H:%M:%S')
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Login exitoso', 'token': token})
    }
