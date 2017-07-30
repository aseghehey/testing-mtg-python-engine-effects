from collections import defaultdict
from enum import Enum

class Mana(Enum):
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4
    COLORLESS = 5


class ManaPool():
    pool = defaultdict(lambda: 0)

    def add(self, mana, amount):
        self.pool[mana] += amount

    # already validated
    def pay(self, manacost):
        for manatype in manacost:
            self.pool[manatype] -= manacost[manatype]

    def clear(self):
        self.pool.clear()