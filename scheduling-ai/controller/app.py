import json
import logging
from Task import Task

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

    task1 = Task(1,"Finish report")
    logger.info(task1)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "task": task1.name,
            "time": task1.scheduled_time,
            # "location": ip.text.replace("\n", "")
        }),
    }
