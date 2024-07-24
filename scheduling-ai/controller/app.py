import json
import logging
import boto3
# from Task import Task
from datetime import datetime, timezone

# import requests
logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    # when a request comes in for a user with a task, this API should add the task to the user's calendar and return the scheduled time for this task.
    # 
    logger.info("---------------------")
    logger.info(event)

    # task1 = Task(1,"Finish report")
    # logger.info(task1)
    dynamo_db_client = boto3.client('dynamodb')

    table_name = "tasks_2"
    item = {
        "task_id": {"S": "1234"},  # Replace with unique task ID
        "user_id": {"S": "user1"},   # Replace with user ID
        "duration": {"N": "3600"},   # Replace with duration in seconds (number as string)
        "scheduled_time": {"S": "2024-07-25T10:00:00Z"},  # Replace with scheduled time in ISO 8601 format
        "task_name": {"S": "Important Meeting"},  # Replace with task name
        "created_at": {"S": str(datetime.now(timezone.utc))},  # Get current UTC time
        "updated_at": {"S": str(datetime.now(timezone.utc))}   # Get current UTC time
    }

    response = dynamo_db_client.put_item(TableName=table_name, Item=item)

    try:
        response = dynamo_db_client.put_item(TableName=table_name, Item=item)
        print(f"PutItem response: {response}")
    except Exception as e:
        print(f"Error writing to DynamoDB: {e}")

    print(f"PutItem response: {response}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            # "task": task1.name,
            # "time": task1.scheduled_time,
            # "location": ip.text.replace("\n", "")
            "task": "successful"
        }),
    }
