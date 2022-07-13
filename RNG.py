from math import floor
from random import random


class RNG:
    def __init__(self, **kwargs):
        seed = kwargs.get('seed', None)
        self.m = 0x80000000  # 2**31
        self.a = 1103515245
        self.c = 12345
        self.state = seed if seed else floor(random() * (self.m - 1))

    def next_int(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self):
        # returns in range [0, 1]
        return self.next_int() / (self.m - 1)

    def next_range(self, start, end):
        #   returns in range [start, end): including start, excluding end
        #   can't modulu nextInt because of weak randomness in lower bits
        range_size = end - start
        random_under_one = self.next_int() / self.m
        return start + floor(random_under_one * range_size)

    def rng_list(self, number_list):
        return number_list[self.next_range(0, len(number_list))]
