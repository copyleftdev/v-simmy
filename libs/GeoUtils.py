import polyline


class PolyTools(object):

    def encode_polylines(self, plines=None):
        return polyline.encode(plines)

    def decode_polylines(self, plines=None):
        return polyline.decode(plines)
