import random
import os
from front_base.random_get_slice import RandomGetSlice

current_path = os.path.dirname(os.path.abspath(__file__))


class SniManager(object):
    plus = ['-', '', "."]
    end = ["com", "net", "ml", "org", "us"]

    def __init__(self, logger):
        self.logger = logger

        fn = os.path.join(current_path, "sni_slice.txt")
        self.slice = RandomGetSlice(fn, 20, '|')

    def get(self):
        return None
