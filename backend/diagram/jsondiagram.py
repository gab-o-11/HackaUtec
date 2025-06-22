import json
import os

def lambda_handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))
        chart_input = data.get("chart")

        if not chart_input:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No se recibió contenido para el diagrama."})
            }

        if isinstance(chart_input, list):
            chart = "\n".join(chart_input)
        elif isinstance(chart_input, str):
            chart = chart_input
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "El formato de 'chart' no es válido. Usa string o lista de líneas."})
            }
        file_path = "/tmp/state_diagram.mmd"
        with open(file_path, "w") as f:
            f.write(chart)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "✅ Diagrama generado exitosamente.",
                "file_path": file_path
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
