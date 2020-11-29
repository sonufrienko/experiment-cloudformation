import requests
from datetime import datetime

server_start_time = datetime.today()

def handler(event, context):
    response = requests.get("https://httpbin.org/ip")
    ip = response.json()["origin"]
    up_time = datetime.today() - server_start_time

    return {
        "start_time": server_start_time.isoformat(),
        "up_time": round(up_time.total_seconds()),
        "ip": ip
    }
