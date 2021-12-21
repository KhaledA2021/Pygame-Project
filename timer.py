import pygame


class timer:

    def __init__(self):
        self.reset_timer()

    def get_current_time(self):
        if self.remaining_time < 1:
            return True
        else:
            return False

    def reset_timer(self):
        self.remaining_time = 0

    def set_new_time(self, input):
        self.remaining_time = input

    def count_down(self):
        self.remaining_time -= 1

