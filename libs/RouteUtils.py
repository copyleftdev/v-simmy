from GoogleUtils import GoogleDirections
from GeoUtils import PolyTools


class RouteGenerator(object):

    def get_route_steps_poly(self, org=None, dest=None):

        go = GoogleDirections()
        plines = go.get_direction_polylines(org, dest)

        pt = PolyTools()
        route_steps = pt.decode_polylines(plines)
        return route_steps
