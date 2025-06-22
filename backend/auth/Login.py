import boto3
import hashlib
import json
from datetime import datetime
import uuid

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def lambda_handler(event, context):
    try:
        # Parsear el JSON del body si es string
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        user_id = body.get("user_id")
        password = body.get("password")

        if not user_id or not password:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Faltan user_id o password"})
            }

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("t_usuariosHack")

        # Buscar al usuario
        response = table.get_item(Key={"user_id": user_id})
        item = response.get("Item")

        if not item:
            return {
                "statusCode": 401,
                "body": json.dumps({"error": "Usuario no encontrado"})
            }

        if item["password"] != hash_password(password):
            return {
                "statusCode": 401,
                "body": json.dumps({"error": "Contraseña incorrecta"})
            }

        # Crear token
        token = str(uuid.uuid4())
        tokens_table = dynamodb.Table("t_tokens_accesoHack")
        tokens_table.put_item(Item={
            "token": token,
            "user_id": user_id,
            "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Login exitoso", "token": token})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }