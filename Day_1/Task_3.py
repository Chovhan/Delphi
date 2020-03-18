import requests
import time


def decorator(function):
    def get_time(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        print(time.time() - start_time)

    return get_time


@decorator
def get_request(url):
    requests.get(url, timeout=5)


resp = get_request("http://google.com")
