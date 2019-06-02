# the base class for all items
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class GoldCoin(Item):
    def __init__(self, amount):
        self.amount = amount
        super(GoldCoin, self).__init__(name="Gold Coin",
                                       description="A single unit of currency.",
                                       value=self.amount)


class Ruby(Item):
    def __init__(self, amount):
        self.amount = amount
        super(Ruby, self).__init__(name="Ruby",
                                   description="A precious ruby, as scarlet as human blood.",
                                   value=100)


# WEAPONS
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(name="Dagger",
                                     description="A old, rusty blade.",
                                     value=5,
                                     damage=5)



