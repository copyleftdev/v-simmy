# -*- coding: utf-8 -*-

import pickle as pkl
import random
import os

p_path  = os.path.dirname(os.path.abspath(__file__))

class PlacesProvider(object):

    def __init__(self):
        self.countries = pkl.load(open("{}/data/countries.p".format(p_path), "rb"))
        self.states = pkl.load(open("{}/data/states.p".format(p_path), "rb"))
        self.places = pkl.load(open("{}/data/places.p".format(p_path), "rb"))

    def get_all_countries(self):
        return self.countries

    def get_all_states(self):
        return self.states

    def get_all_places(self):
        return self.places

    def get_random_country(self):
        return random.choice(self.countries)

    def get_random_state(self):
        return random.choice(self.states)

    def get_random_supported_place(self):
        return random.choice(self.places)

    def get_random_country_and_place(self):
        country, place = [
            random.choice(self.countries),
            random.choice(self.places)
        ]
        rnd_dict = {"country": random.choice(self.countries),
                    "place": random.choice(self.places),
                    "api_query": "{}+in+{}".format(place, country)}

        return rnd_dict

    def get_random_state_and_place(self):
        state, place = [
            random.choice(self.states),
            random.choice(self.places)
        ]
        rnd_dict = {"state": random.choice(self.states),
                    "place": random.choice(self.places),
                    "api_query": "{}+in+{}".format(place, state)}
        return rnd_dict


p = PlacesProvider()
print(p.get_random_state_and_place())
