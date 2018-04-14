from libs.GoogleUtils import GoogleDirections, GooglePlacesTextSearch
from libs.GeoUtils import PolyTools
from libs.PlacesUtils import PlacesProvider
import random


class RouteGenerator(object):

        def __init__(self):
            self.go = GoogleDirections()
            self.pt = PolyTools()
            self.pl = GooglePlacesTextSearch()
            self.pp = PlacesProvider()

        def get_route_poly(self, org=None, dest=None):
            plines = self.go.get_direction_polylines(org, dest)
            route_steps = self.pt.decode_polylines(plines)
            return route_steps

        def get_route_json(self, org=None, dest=None):
            full_details = self.go.get_full_directions_payload(org, dest)
            steps = []
            for r in full_details['routes']:
                for l in r['legs']:
                    for s in l['steps']:
                        steps.append(s)
            return steps

        def get_route_loop(self, org=None, dest=None):
            steps = []
            seg_a = self.go.get_full_directions_payload(org, dest)
            seg_b = self.go.get_full_directions_payload(dest, org)

            for r in seg_a['routes']:
                for l in r['legs']:
                    for s in l['steps']:
                        steps.append(s)

            for r in seg_b['routes']:
                for l in r['legs']:
                    for s in l['steps']:
                        steps.append(s)
            return steps
