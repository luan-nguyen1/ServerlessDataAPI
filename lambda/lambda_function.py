import json
import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")  # Log incoming request

    try:
        http_method = event.get("httpMethod", "")

        # Handle GET Request
        if http_method == "GET":
            query_params = event.get("queryStringParameters", {})
            if query_params and "id" in query_params:
                return {
                    "statusCode": 200,
                    "body": json.dumps({"message": "Data retrieved!", "id": query_params["id"]})
                }
            else:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Missing 'id' parameter in query"})
                }

        # Handle POST Request
        elif http_method == "POST":
            if "body" not in event:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "No body provided"})
                }

            body = json.loads(event["body"])
            logger.info(f"Parsed body: {body}")  # Log parsed data

            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Data saved!", "id": body.get("id", "N/A")})
            }

        # Unsupported HTTP Method
        else:
            return {
                "statusCode": 405,
                "body": json.dumps({"error": f"Method {http_method} not allowed"})
            }

    except json.JSONDecodeError as json_error:
        logger.error(f"JSON parsing error: {str(json_error)}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format"})
        }
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
