import time
import requests

TEN_MINUTES = 60 * 10

while True:
    try:
        requests.get('https://codefather.dev')
    except Exception:
        pass
    print(1)
    time.sleep(TEN_MINUTES)
