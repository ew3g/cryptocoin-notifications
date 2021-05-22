from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from requests.sessions import session

def get_request(url, headers=None, params=None):
    try:
        session = Session()
        if headers:
            session.headers.update(headers)
        
        response = session.get(url, params=params)
        return json.loads(response.text.encode('ascii', 'ignore'))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

def post_request(url, headers=None, data=None):
    try:
        session = Session()
        session.post(url, data=data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)