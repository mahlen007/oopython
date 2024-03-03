#!/usr/bin/env python3
"""
Class for Players
"""

from src.queue import Queue

class Game():
    """ class Game """
    def __init__(self):
        #self._items = []
        self.players=Queue()
        self.round_score=[]

    def round_score_to_list(self):
        """ Score to list """
        new_list = []
        for g in self.round_score:
            new_list.append((g.owner, g.points))
        return new_list

    def round_score_from_list(self,my_list):
        """ Fill the queue from a list """
        for item in my_list:
            self.round_score.append(item)

    def highest_score(self):
        """ Find the highest score """
        max_=0
        for _, value in self.round_score:
            if value>max_:
                max_=value
        return max_

    def winner(self):
        """ Find the winner """
        max_=0
        owner=0
        for key, value in self.round_score:
            if value>max_:
                owner=key
                max_=value
        return owner
