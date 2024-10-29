from dns import resolver
import requests
import os

prefix = os.environ["LAMBDA_TASK_ROOT"]

resolver.override_system_resolver(resolver.Resolver(f"{prefix}/resolv.conf"))


def lambda_handler(event, context):
    res = requests.get("https://www.google.com")
    return {"statusCode": res.status_code, "body": res.text}
