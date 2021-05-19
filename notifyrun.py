import requester
import secret

class Constant:
    URL_NOTIFICATION = secret.NOTIFY_RUN_URL

constant = Constant()

def notify(message):
    requester.post_request(constant.URL_NOTIFICATION, data=message)
