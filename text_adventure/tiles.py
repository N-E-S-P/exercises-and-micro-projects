import items, enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingRoom(MapTile):
    def intro_text(self):
        return '''
        You wake up in a dark, damp room made of stone. 
        There is a flickering torch on the wall. You can
        see there is a wooden door at the other side of 
        the room.'''

    def modify_player(self, player):
        # Room has no effect on player
        pass


class LootRoom(MapTile):
    def __init__(self, item):
        self.item = item
        super(LootRoom, self).__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, enemy):
        self.enemy = enemy
        super(EnemyRoom, self).__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy attacks! It does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))


