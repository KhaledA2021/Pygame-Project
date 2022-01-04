import pygame


class timer:

    def __init__(self):
        self.remaining_time = None

    def set_new_time(self, input):
        self.remaining_time = input

    def count_down(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
        elif self.remaining_time <= 0:
            return True


