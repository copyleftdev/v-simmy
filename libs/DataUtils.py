
import requests

class RestRouter(object):

    def __init__(self, host,route):
        self.host = host
        self.route = route

    def send_post(self, payload):
        header = {"Content-Type":"application/json"}
        url = "http://{}{}".format(self.host, self.route)
        req = requests.post(url, data=payload, headers=header)
