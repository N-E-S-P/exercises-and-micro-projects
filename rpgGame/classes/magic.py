import random


class Spell:

    def __init__(self, name, cost, dmg, func):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.func = func

    def generate_damage(self):
        low_dmg = self.dmg - 10
        high_dmg = self.dmg + 10
        return random.randrange(low_dmg, high_dmg)
