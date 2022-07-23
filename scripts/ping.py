import time
import requests

TEN_MINUTES = 60 * 10

while True:
    try:
        requests.get('https://codefather.dev')
    except Exception:
        pass
    time.sleep(TEN_MINUTES)
