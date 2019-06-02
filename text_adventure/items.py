# the base class for all items
class Item:
    def __init__(self, name, description, value, amount):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value, self.amount)


class GoldCoin(Item):
    def __init__(self, amount):
        self.amount = amount
        super(GoldCoin, self).__init__(name="Gold Coin",
                                       description="A single unit of currency.",
                                       value=self.amount,
                                       amount=self.amount)


class Ruby(Item):
    def __init__(self):
        super(Ruby, self).__init__(name="Ruby",
                                   description="A precious ruby, as scarlet as human blood.",
                                   value=100,
                                   amount=self.amount)


class Key(Item):
    def __init__(self):
        super(Key, self).__init__(name="Key",
                                  description="A small, rusty key.",
                                  value=0,
                                  amount=self.amount)


class Arrow(Item):
    def __init__(self):
        super(Arrow, self).__init__(name="Arrow",
                                    description="A sharp arrow, to be used with a bow.",
                                    value=1,
                                    amount=self.amount)


class Rope(Item):
    def __init__(self):
        super(Rope, self).__init__(name="Rope",
                                   description="A hemp rope, useful for overcoming obstacles.",
                                   value=15,
                                   amount=self.amount)


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


class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__(name="Bow",
                                  description="A wooden bow, good for hunting.",
                                  value=10,
                                  damage=5)

