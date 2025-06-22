import boto3
import hashlib
import json
from datetime import datetime

# Función para hashear contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def lambda_handler(event, context):
    try:
        # Obtener los datos del body
        user_id = event.get('user_id')
        password = event.get('password')

        # Validación de campos
        if not user_id or not password:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing user_id or password'})
            }

        # Conectar con DynamoDB
        dynamodb = boto3.resource('dynamodb')
        t_usuarios = dynamodb.Table('t_usuarios')

        # Verificar si el usuario ya existe
        response = t_usuarios.get_item(Key={'user_id': user_id})
        if 'Item' in response:
            return {
                'statusCode': 409,
                'body': json.dumps({'error': 'User already exists'})
            }

        # Hashear contraseña
        hashed_password = hash_password(password)

        # Registrar usuario
        t_usuarios.put_item(
            Item={
                'user_id': user_id,
                'password': hashed_password,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User registered successfully',
                'user_id': user_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
