import requests

API_BASE_URL = "https://maps.googleapis.com"
DIR_API_KEY = "AIzaSyAOJbDafHsGHOG7zukkTFAM0SL0XzRypE0"
PLACE_API_KEY = "AIzaSyC7RihmXZa33NPiUpXOSM-5_9Nalyiqwpg"


class GooglePlacesTextSearch(object):

    def __init__(self):
        self.base_url = API_BASE_URL
        self.tsroute = "/maps/api/place/textsearch/json"
        self.dtlroute = "/maps/api/place/details/json"

    def get_places_via_query(self, query=None, radius=100):
        params = "?query={}&key={}&radius={}".format(query, PLACE_API_KEY,
                                                     radius)
        req = requests.get(self.base_url + self.tsroute + params)
        res = req.json()
        return res

    def get_list_of_adresses(self, query=None, radius=100):
        params = "?query={}&key={}&radius={}".format(query, PLACE_API_KEY,
                                                     radius)
        req = requests.get(self.base_url + self.tsroute + params)
        res = req.json()
        address_list = []
        for a in res['results']:
            address_list.append(a['formatted_address'])
        return address_list

    def get_place_details_by_placeid(self, pid=None):
        params = "?placeid={}&key={}".format(pid, PLACE_API_KEY)
        req = requests.get(self.base_url + self.dtlroute + params)
        res = req.json()
        return res

    def get_placeid_from_address(self, address=None):
        query = address.replace(",", "").replace(" ", "+")
        params = "?query={}&key={}".format(query, PLACE_API_KEY)
        req = requests.get(self.base_url + self.tsroute + params)
        res = req.json()
        for p in res['results']:
            return p['place_id']


class GoogleDirections(object):

    def __init__(self):
        self.base_url = API_BASE_URL
        self.dirroute = "/maps/api/directions/json"

    def get_full_directions_payload(self, org=None, dest=None):
        params = """?origin={}&destination={}&key={}""".format(org, dest,
                                                               DIR_API_KEY)
        req = requests.get(self.base_url + self.dirroute + params)
        res = req.json()
        return res

    def get_direction_polylines(self, org=None, dest=None):
        params = """?origin={}&destination={}&key={}""".format(org, dest,
                                                               DIR_API_KEY)
        req = requests.get(self.base_url + self.dirroute + params)
        res = req.json()
        for plo in res['routes']:
            return plo['overview_polyline']['points']
