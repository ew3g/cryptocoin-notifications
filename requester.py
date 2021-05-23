from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_request(url, headers=None, params=None):
    try:
        session_request = Session()
        if headers:
            session_request.headers.update(headers)

        response = session_request.get(url, params=params)
        return json.loads(response.text.encode('ascii', 'ignore'))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def post_request(url, headers=None, data=None):
    try:
        session_request = Session()
        session_request.post(url, data=data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
