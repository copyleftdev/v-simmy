from libs.RouteUtils import RouteGenerator
from libs.GoogleUtils import GooglePlacesTextSearch
from libs.DataUtils import RestRouter
import time
from geopy.geocoders import Nominatim
import arrow
import random
import json


class CarSim(object):
    def __init__(self, sim_id=None):

        self.sim_id = sim_id

    def sim_init(self, static_vectors=False):
        geolocator = Nominatim()
        post_status = RestRouter("127.0.0.1:8000", "/sim_status")

        pl = GooglePlacesTextSearch()
        if static_vectors is False:

            addl1 = pl.get_list_of_adresses("resterants+in+Pasadena+Ca")
            addl2 = pl.get_list_of_adresses("movie_theater+in+Pasadena+Ca")
            add1 = random.choice(addl1)
            add2 = random.choice(addl2)
        else:
            add1 = "760 W Naomi Ave, Arcadia, CA 91007"
            add2 = "1325 S Baldwin Ave, Arcadia, CA 91007"

        c = RouteGenerator()
        payload = c.get_route_loop(add1, add2)

        totalt = arrow.utcnow()
        tlocal = totalt.to('US/Pacific')

        for d in payload:
            html_intruction_detail = d['html_instructions']
            cur_str_lat = d['start_location']['lat']
            cur_start_lng = d['start_location']['lng']
            cur_end_lat = d['end_location']['lat']
            cur_end_lng = d['end_location']['lng']
            distance_text = d['distance']['text']
            distance_value = d['distance']['value']
            duration_text = d['duration']['text']
            duration_value = d['duration']['value']

            start_tag = geolocator.reverse("{}, {}".format(cur_str_lat,
                                                           cur_start_lng))
            end_tag = geolocator.reverse("{}, {}".format(cur_end_lat,
                                                         cur_end_lng))
            utc = arrow.utcnow()
            local = utc.to('US/Pacific')

            sim_from_status = {'sim_id': self.sim_id,
                               'from_address': str(start_tag),
                               'from_cord': [cur_str_lat,
                                             cur_start_lng],
                               'from_time': str(utc),
                               'instruction': html_intruction_detail}
            post_status.send_post(json.dumps(sim_from_status))
            print(sim_from_status)
            time.sleep(duration_value)
            sim_to_status = {'sim_id': self.sim_id, 'to_address': str(end_tag),
                             'to_cord': [cur_end_lat, cur_end_lng],
                             'to_time': str(utc), 'elapsed': local.humanize()}
            post_status.send_post(json.dumps(sim_to_status))
            print(sim_to_status)
