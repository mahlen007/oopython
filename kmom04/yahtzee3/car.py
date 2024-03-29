#!/usr/bin/env python3
"""
Contains the Car class.
"""
class Car():
    """ Car class that handles cars with model and price. """
    wheels = 4

    def __init__(self, model, price):
        """ Constuctor """
        self.model = model
        self.price = price

    def present_car(self):
        """ Returns a string presenting the car """
        return f"This car is of model {self.model} and costs {self.price}$."
