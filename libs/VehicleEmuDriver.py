from lib.RouteUtils import RouteGenerator
import uuid


class Vehicle(object):
    def __init__(self, v_id, max_speed):
        self.v_id = v_id
        self.max_speed = max_speed


class CarSim(Vehicle):
    def __init__(self):
        self.rg = RouteGenerator()

    def sim_init_poly(self):
        pass

    def sim_init_json(self):
        pass
