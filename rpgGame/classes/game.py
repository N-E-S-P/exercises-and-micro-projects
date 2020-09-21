import random


class Character:

    def __init__(self, name, hp, mp, atk, df, mag, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.mag = mag
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_phys_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(self.name + "'s turn:")
        for action in self.actions:
            print('    ', str(i) + ":", action)
            i += 1

    def choose_mag(self):
        i = 1
        print('MAGIC:')
        for magic in self.mag:
            print('    ', str(i) + ":", magic.name, "-- Cost:", magic.cost)
            i += 1

    def choose_item(self):
        i = 1
        print('ITEMS:')
        for item in self.items:
            print('    ', str(i) + ":", item.name, "x", item.quantity)
            i += 1

    def choose_target(self, targets):
        i = 1
        print('TARGET:')
        for target in targets:
            print('    ', str(i) + ":", target.name)
            i += 1
        choice = int(input('    Choose the target:')) - 1
        return choice

    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.max_hp) * 100 // 4

        while hp_bar_ticks > 0:
            hp_bar += '█'
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        mp_bar = ""
        mp_bar_ticks = (self.mp / self.max_mp) * 100 // 10

        while mp_bar_ticks > 0:
            mp_bar += '█'
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += ' '
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + '/' + str(self.max_mp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += ' '
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(self.name + '     ' + current_hp, '|' + hp_bar + '|' + '\n               '
              + current_mp, '|' + mp_bar + '|' + '\n')


