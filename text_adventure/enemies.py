class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp


class Spider(Enemy):
    def __init__(self):
        super(Spider, self).__init__(name="Spider",
                                     hp=5,
                                     damage=2)


class Acolyte(Enemy):
    def __init__(self):
        super(Acolyte, self).__init__(name="Acolyte",
                                      hp=15,
                                      damage=5)


class Ghoul(Enemy):
    def __init__(self):
        super(Ghoul, self).__init__(name="Ghoul",
                                    hp=25,
                                    damage=10)


class ThingInTheDark(Enemy):
    def __init__(self):
        super(ThingInTheDark, self).__init__(name="Thing in the Dark",
                                             hp=75,
                                             damage=20)

