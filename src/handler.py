import json
import requests


def hello(event, context):
    # Send a GET request to a public API
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    print(response.content)

    body = {"message": str(response.content)}

    return {"statusCode": 200, "body": json.dumps(body)}
