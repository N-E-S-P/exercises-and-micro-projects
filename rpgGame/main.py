from classes.game import Character
from classes.magic import Spell
from classes.inventory import Item
import random

# Magic
force_push = Spell("Force Push", 10, 60, 'attack')
mend = Spell("Mend", 15, 70, 'heal')

# Items
potion = Item('Potion', 'heal', 'Heals for 50 HP.', 50, 5)
throwing_knife = Item('Throwing knife', 'attack', 'Inflicts 50 points of damage', 50, 5)

# Characters
player1 = Character('STRIDER ', 320, 30, 40, 40, [], [potion, throwing_knife])
player2 = Character('CONTROL ', 280, 100, 20, 20, [force_push, mend], [])
players = [player1, player2]

# Enemies
enemy1 = Character('Overlord', 20, 200, 60, 60, [], [])
enemy2 = Character('Servant ', 20, 200, 20, 20, [force_push], [])
enemies = [enemy1, enemy2]

running = True
i = 0

print('\n')
print('An enemy attacks!')
print('\n')

while running:
    for player in players:
        player.get_stats()
    for enemy in enemies:
        enemy.get_stats()
    print('\n')

    # Players' turn
    for player in players:
        if player.get_hp() == 0:
            continue
        player.choose_action()
        print('======================================================')
        choice = input('Choose an action: ')
        choice = int(choice) - 1

        if choice == 0:
            dmg = player.generate_phys_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(player.name.replace(' ', ''), 'attacks', enemies[enemy].name.replace(' ', ''), 'for', dmg, 'points of damage!')
            print('\n')
        elif choice == 1:
            player.choose_mag()
            magic_choice = input('Choose a spell:')
            magic_choice = int(magic_choice) - 1
            if magic_choice == -1:
                continue
            spell_cast = player.mag[magic_choice]
            if spell_cast.cost > player.get_mp():
                print('You have not enough MP to cast this spell!')
                print('\n')
                continue
            player.reduce_mp(spell_cast.cost)
            if spell_cast.func == 'heal':
                magic_dmg = spell_cast.generate_damage()
                ally = player.choose_target(players)
                players[ally].heal(magic_dmg)
                print(player.name.replace(' ', ''), 'casts', spell_cast.name + '!', players[ally].name.replace(' ', ''), 'is healed for', magic_dmg, 'HP.')
                print('\n')
            elif spell_cast.func == 'attack':
                magic_dmg = spell_cast.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(player.name.replace(' ', ''), 'casts', spell_cast.name + '!', enemies[enemy].name.replace(' ', ''), 'takes', magic_dmg, 'points of damage.')
                print('\n')
        elif choice == 2:
            player.choose_item()
            item_choice = input('Choose an item:')
            item_choice = int(item_choice) - 1
            if item_choice == -1:
                continue
            item_used = player.items[item_choice]
            if item_used.quantity == 0:
                print('You don\'t have any', item_used.name, 'left!')
                print('\n')
                continue
            else:
                item_used.quantity -= 1
                if item_used.func == 'heal':
                    ally = player.choose_target(players)
                    players[ally].heal(item_used.prop)
                    print(player.name.replace(' ', ''), 'used', item_used.name + '!', players[ally].name.replace(' ', ''), 'is healed for', item_used.prop, 'HP.')
                    print('\n')
                elif item_used.func == 'attack':
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item_used.prop)
                    print(player.name.replace(' ', ''), 'used', item_used.name + '!', enemies[enemy].name.replace(' ', ''), 'takes', item_used.prop, 'points of damage.')
                    print('\n')

    # Victory / defeat conditions
    defeated_players = 0
    defeated_enemies = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            del enemy
            defeated_enemies += 1
    if defeated_enemies == len(enemies):
        print('You won the battle!')
        running = False
        break

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    if defeated_players == len(players):
        print('You lost...')
        running = False
        break

    # Enemies' turn
    for enemy in enemies:
        enemy_turn = True
        enemy_choice = random.randrange(0, 2)
        target = random.randint(0, 1)

        while enemy_turn:
            if enemy_choice == 0:
                enemy_dmg = enemy.generate_phys_damage()
                players[target].take_damage(enemy_dmg)
                print(enemy.name, 'attacks for', enemy_dmg, 'points of damage.')
                print('\n')
                enemy_turn = False

            elif enemy_choice == 1:
                if len(enemy.mag) == 0:
                    enemy_turn = True
                else:
                    enemy_magic_choice = random.randrange(0, len(enemy.mag))
                    spell_cast = enemy.mag[enemy_magic_choice]
                    if spell_cast.cost > enemy.get_mp():
                        enemy_turn = True
                    enemy.reduce_mp(spell_cast.cost)
                    if spell_cast.func == 'heal':
                        magic_dmg = spell_cast.generate_damage()
                        ally = enemy.choose_target(enemies)
                        enemies[ally].heal(magic_dmg)
                        print(enemy.name.replace(' ', ''), 'casts', spell_cast.name + '!', enemies[ally].name.replace(' ', ''), 'is healed for', magic_dmg, 'HP.')
                        print('\n')
                        enemy_turn = False
                    elif spell_cast.func == 'attack':
                        magic_dmg = spell_cast.generate_damage()
                        player = enemy.choose_target(players)
                        players[player].take_damage(magic_dmg)
                        print(enemy.name.replace(' ', ''), 'casts', spell_cast.name + '!', players[player].name.replace(' ', ''), 'takes', magic_dmg, 'points of damage.')
                        print('\n')
                        enemy_turn = False

            elif enemy_choice == 2:
                if len(enemy.items) == 0:
                    enemy_turn = True
                else:
                    enemy_item_choice = random.randint(0, len(enemy.items))
                    item_used = enemy.items[enemy_item_choice]
                    if item_used.quantity == 0:
                        enemy_turn = True
                    else:
                        item_used.quantity -= 1
                        if item_used.func == 'heal':
                            ally = enemy.choose_target(enemies)
                            enemies[ally].heal(item_used.prop)
                            print(enemy.name.replace(' ', ''), 'used', item_used.name + '!', enemies[ally].name.replace(' ', ''), 'is healed for', item_used.prop, 'HP.')
                            print('\n')
                            enemy_turn = False
                        elif item_used.func == 'attack':
                            player = enemy.choose_target(players)
                            players[player].take_damage(item_used.prop)
                            print(enemy.name.replace(' ', ''), 'used', item_used.name + '!', players[player].name.replace(' ', ''), 'takes', item_used.prop, 'points of damage.')
                            print('\n')
                            enemy_turn = False
