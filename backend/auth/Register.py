import boto3
import hashlib
import json
from datetime import datetime

# Función para hashear la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def lambda_handler(event, context):
    try:
        # Parsear el JSON del body si es un string
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        # Obtener user_id y password
        user_id = body.get("user_id")
        password = body.get("password")

        # Validar que no estén vacíos
        if not user_id or not password:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing user_id or password"})
            }

        # Conectar a DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("t_usuariosHack")

        # Verificar si el usuario ya existe
        response = table.get_item(Key={"user_id": user_id})
        if "Item" in response:
            return {
                "statusCode": 409,
                "body": json.dumps({"error": "User already exists"})
            }

        # Insertar usuario con contraseña hasheada
        table.put_item(Item={
            "user_id": user_id,
            "password": hash_password(password),
            "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "User registered successfully",
                "user_id": user_id
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }