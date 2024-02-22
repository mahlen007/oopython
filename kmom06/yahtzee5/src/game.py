#!/usr/bin/env python3
"""
Class for Players
"""

from src.scoreboard import Scoreboard
from src.queue import Queue
import src.sort

class Game():
    def __init__(self):
        #self._items = []
        self.players=Queue()

