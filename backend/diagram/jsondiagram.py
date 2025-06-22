import json
import os

def lambda_handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))

        chart_lines = data.get("chart", [])

        if not chart_lines or not isinstance(chart_lines, list):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No se recibieron líneas para el diagrama."})
            }

        chart = "\n".join(chart_lines)


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
