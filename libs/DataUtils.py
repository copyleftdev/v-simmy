
import requests

class RestRouter(object):

    def __init__(self, host,route):
        self.host = host
        self.route = route

    def send_post(self, payload):
        header = {"content-type":"application/json"}
        url = "http://{}/{}".format(self.host, self.route)
        req = requests.post(url, data=payload, header=header)

    def get_res(self, params):
        url = "{}:{}/{}{}".format(self.host, self.port, self.route, params)
        req = requests.post(url)
