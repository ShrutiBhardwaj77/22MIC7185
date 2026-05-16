import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzaHJ1dGliMDQxMUBnbWFpbC5jb20iLCJleHAiOjE3Nzg5Mjg1NjUsImlhdCI6MTc3ODkyNzY2NSwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjE3NWMwYjNlLTY0NGYtNGY0OS05NmJkLWE5YTA3NTAwNTg5NyIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNocnV0aSBiaGFyZHdhaiIsInN1YiI6IjhkZTdjYTU4LTQ2ZDQtNDhjMC1iODAzLWM4Njk1MjNmMjQ3MiJ9LCJlbWFpbCI6InNocnV0aWIwNDExQGdtYWlsLmNvbSIsIm5hbWUiOiJzaHJ1dGkgYmhhcmR3YWoiLCJyb2xsTm8iOiIyMm1pYzcxODUiLCJhY2Nlc3NDb2RlIjoiU2ZGdVdnIiwiY2xpZW50SUQiOiI4ZGU3Y2E1OC00NmQ0LTQ4YzAtYjgwMy1jODY5NTIzZjI0NzIiLCJjbGllbnRTZWNyZXQiOiJYRmNmZ05SY1RrakFnc05LIn0.fORm8lEhcQGtrUUYTxLN0LiXpemy0F2sY5bVYpri6zw"

BASE_URL = "http://4.224.186.213/evaluation-service/logs"


def Log(stack, level, package, message):

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(
        BASE_URL,
        json=payload,
        headers=headers
    )

    print(response.json())