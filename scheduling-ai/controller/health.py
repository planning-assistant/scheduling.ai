import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            # "task": task1.name,
            # "time": task1.scheduled_time,
            # "location": ip.text.replace("\n", "")
            "health": "ok"
        }),
    }