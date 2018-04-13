from libs.GoogleUtils import GoogleDirections
from libs.GeoUtils import PolyTools


class RouteGenerator(object):

        def __init__(self):
            self.go = GoogleDirections()
            self.pt = PolyTools()

        def get_route_steps_poly(self, org=None, dest=None):
            plines = self.go.get_direction_polylines(org, dest)
            route_steps = self.pt.decode_polylines(plines)
            return route_steps

        def get_full_route_details(self, org=None, dest=None):
            full_details = self.go.get_full_directions_payload(org, dest)
            return full_details
