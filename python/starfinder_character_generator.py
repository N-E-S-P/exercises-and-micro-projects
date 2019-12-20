import random

races = ['Android', 'Human', 'Kasatha', 'Lashunta', 'Shirren', 'Vesk', 'Ysoki']

classes = ['Envoy', 'Mechanic', 'Mystic', 'Operative', 'Solarian', 'Soldier', 'Technomancer']

themes = ['Ace Pilot', 'Biotechnician', 'Bounty Hunter', 'Career Trooper', 'Colonist', 'Corporate Agent',
          'Cultist', 'Cyberborn', 'Death-Touched', 'Dragonblood', 'Dream Prophet', 'Gladiator', 'Icon',
          'Mercenary', 'Outlaw', 'Paranormal Investigator', 'Priest', 'Roboticist', 'Scholar', 'Solar Disciple',
          'Space Pirate', 'Spacefarer', 'Tempered Pilgram', 'Themeless', 'Tinker', 'Wild Warden', 'Xenoarchaeologist',
          'Xenoseeker']

skills = ['Acrobatics', 'Athletics', 'Bluff', 'Computers', 'Culture', 'Diplomacy', 'Disguise', 'Engineering',
          'Intimidate', 'Life Science', 'Medicine', 'Mysticism', 'Perception', 'Physical Science', 'Piloting',
          'Profession', 'Sense Motive', 'Sleight of Hand', 'Stealth', 'Survival']

connections = ['Akashic', 'Devastator', 'Empath', 'Flamewalker', 'Geneturge', 'Healer', 'Mindbreaker', 'Overlord',
               'Shadow', 'Star Shaman', 'Xenodruid']

mspells1 = ['Baleful Polymorph', 'Battlemind Link (Lesser)', 'Carnivorous', 'Charm Person', 'Command',
            'Confusion (Lesser)', 'Detect Augmentation', 'Detect Radiation', 'Detect Thoughts', 'Disguise Self', 'Fear',
            'Gloom Mote', 'Identify', 'Keen Senses', 'Life Bubble', 'Might of the Ellicoth', 'Mind Link', 'Mind Thrust',
            'Mystic Cure', 'Necromantic Revitalization', 'Polymorph', 'Pyre Wreath', 'Reflecting Armor',
            'Remove Condition (Lesser)', 'Seeking Shot', 'Share Language', 'Slithering Chain', 'Summon Creature',
            'Wisp Ally']

mspells2 = ['Augury', 'Baleful Polymorph', 'Command Undead', 'Darkvision', 'Daze Monster', 'Emberstep', 'Fear',
            'Fog Cloud', 'Force Blast', 'Hold Person', 'Hurl Forcedisk', 'Inflict Pain', 'Mind Thrust', 'Mystic Cure',
            'Necromantic Revitalization', 'Paranoia', 'Polymorph', 'Reject Augmentation', 'Remove Condition',
            'Restoration (Lesser)', 'See Invisibility', 'Shield Other', 'Spider Climb', 'Status', 'Summon Creature',
            'Zone of Truth']

mspells3 = ['Baleful Polymorph', 'Bestow Curse', 'Burning Ash Clouds', 'Charm Monster', 'Clairaudience/Clairvoyance',
            'Deep Slumber', 'Dispel Magic', 'Fear', 'Haste', 'Hologram Memory', 'Irradiate', 'Mental Block',
            'Mind Thrust', 'Mystic Cure', 'Necromantic Revitalization', 'Nightmare', 'Polymorph',
            'Psychokinetic Strangulation', 'Ray of Exhaustion', 'Remove Affliction', 'Resistant Armor (Lesser)',
            'Slow', 'Speak with Dead', 'Suggestion', 'Summon Creature', 'Synaptic Pulse', 'Tongues',
            'Umbral Tendril', 'Viral Destruction']

mspells4 = ['Animate Dead', 'Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Borrow Corruption', 'Confusion',
            'Control Atmosphere', 'Cosmic Eddy', 'Death Ward', 'Dimensional Anchor', 'Discern Lies', 'Dismissal',
            'Divination', 'Enervation', 'Fear', 'Hold Monster', 'Mind Probe', 'Mind Thrust', 'Mystic Cure',
            'Necromantic Revitalization', 'Planar Binding', 'Polymorph (Mass)', 'Polymorph', 'Read the Flames',
            'Reincarnate', 'Remove Radioactivity', 'Resistant Armor', 'Restoration', 'Shadow Jump', 'Summon Creature',
            'Telepathic Bond']

mspells5 = ['Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Battlemind Link', 'Break Enchantment', 'Call Cosmos',
            'Command (Greater)', 'Commune With Nature', 'Contact Other Plane', 'Crush Skull', 'Dismissal',
            'Dispel Magic (Greater)', 'Dominate Person', 'Feeblemind', 'Mind Thrust', 'Modify Memory',
            'Mystic Cure (Mass)', 'Necromantic Revitalization', 'Planar Binding', 'Polymorph (Mass)', 'Polymorph',
            'Raise Dead', 'Reanimate', 'Remove Condition (Greater)', 'Resistant Aegis', 'Retrocognition',
            'Shadow Body', 'Summon Creature', 'Synaptic Pulse (Greater)', 'Telepathy', 'Waves of Fatigue']

mspells6 = ['Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Control Gravity', 'Control Undead', 'Enshrining Refuge',
            'Ethereal Jaunt', 'Flesh to Stone', 'Gravitational Singularity', 'Inflict Pain (Mass)', 'Mind Swap',
            'Mind Thrust', 'Mystic Cure (Mass)', 'Mystic Cure', 'Necromantic Revitalization', 'Planar Barrier',
            'Planar Binding', 'Plane Shift', 'Polymorph (Mass)', 'Psychic Surgery', 'Regenerate',
            'Resistant Armor (Greater)', 'Shadow Walk', 'Snuff Life', 'Subjective Relative', 'Suggestion (Mass)',
            'Summon Creature', 'Telepathic Jaunt', 'True Seeing', 'Vision']

ais = ['Combat Drone', 'Hover Drone', 'Stealth Drone', 'Exocortex']

tricks = ['Combat Maintenance', 'Distracting Hack', 'Energy Shield', 'Hack Directory', 'Neural Shunt',
          'Nightvision Processor', 'Overcharge', 'Overclocking', 'Overload Weapon', 'Portable Power',
          'Provisional Repair', 'Quick Patch', 'Quick Repair', 'Recalibrate Engine', 'Repair Drone',
          'Tech Tinkerer', 'Visual Data Processor', 'Boost Shield', 'Drone Meld', 'Engineer\'s Eye',
          'Ghost Intrusion', 'Holographic Projector', 'Hyperclocking', 'Improved Overcharge',
          'Invisibility Bypass Processor', 'Mobile Armory', 'Recalibrate Weapon', 'Resistant Energy',
          'Scoutbot', 'Technological Innovator', 'Extra Mod', 'Improved Resistant Energy',
          'Invisibility-Hampering Projector', 'Melded Mod', 'Mod Tinkerer', 'Saboteur', 'Scoutbot Mod',
          'Superior Overcharge', 'Ultraclocking']

exploits = ['Alien Archive', 'Armor Optimizer', 'Combat Trick', 'Concealed Weaponry', 'Disarming Attack',
            'Elite Saboteur', 'Field Treatment', 'Holographic Clone', 'Inoculation', 'Jack of All Trades',
            'Lightning Reload', 'Nightvision', 'Pistol Whip', 'Quick Disguise', 'Trap Spotter', 'Uncanny Mobility',
            'Uncanny Pilot', 'Bleeding Shot', 'Certainty', 'Debilitating Sniper', 'Enhanced Senses', 'Fast Aim',
            'Hampering Shot', 'Improved Quick Movement', 'Interfering Shot', 'Knee Shot', 'Mentalist\'s Bane',
            'Operative Pounce', 'Ricochet Shot', 'Speed Hacker', 'Staggering Shot', 'Stalwart', 'Sure-Footed',
            'Uncanny Shooter', 'Blinding Shot', 'Cloacking Field', 'Deactivating Shot', 'Elusive Hacker',
            'Ever Vigilant', 'Extended Debilitation', 'Glimpse the Truth', 'Holographic Distraction',
            'Improved Evasion', 'Improved Uncanny Mobility', 'Master of Disguise', 'Optical Optimization',
            'Stunning Shot', 'Utility Belt', 'Versatile Movement', 'Efficient Cloaking Filed', 'Knockout Shot',
            'Multiattack Mastery', 'Surveillance Wraith', 'Uncanny Senses']

specializations = ['Daredevil', 'Detective', 'Explorer', 'Gadgeteer', 'Ghost', 'Hacker', 'Spy', 'Thief']

fighting_styles = ['Arcane Assailant', 'Armor Storm', 'Blitz', 'Bombard', 'Gloom Gunner', 'Guard', 'Hit-and-Run',
                   'Sharpshoot', 'Shock and Awe']

boosts = ['Anchoring Arcana', 'Armored Advantage', 'Blazing Strike', 'Brutal Blast', 'Bullet Barrage', 'Caustic Burns',
          'Deflecting Smash', 'Electric Arc', 'Flash Freeze', 'Heavy Onslaught', 'Laser Accuracy', 'Massive Momentum',
          'Melee Striker', 'Plasma Immolation', 'Powerful Explosive', 'Raw Lethality', 'Sonic Resonance',
          'Steady Sniper', 'Twinned Threat', 'Unarmed Mauler', 'Unstoppable Strike', 'Unyelding Bulwark']

improvisations = ['Brace Yourselves', 'Clever Faint', 'Coordinated Reload', 'Dispiriting Taunt', 'Don\'t Quit',
                  'Expanded Attunement', 'Fire Support', 'Get\'Em', 'Inspiring Boost', 'Look Alive', 'Not in the Face',
                  'Quick Quaff', 'Universal Expression', 'Watch Your Step', 'Clever Attack', 'Duck Under', 'Focus',
                  'Hurry', 'Long-Range Improvisation', 'Quick Dispiriting Taunt', 'Quick Inspiring Boost',
                  'Terrifying Blast', 'Watch Out', 'Bedside Manner', 'Clever Improvisations', 'Draw Fire', 'Heads Up',
                  'Improved Get\'Em', 'Trust Your Gear', 'Desperate Defense', 'Expert Attack', 'Hidden Agenda',
                  'Improved Brace Yourselves', 'Improved Hurry', 'Improved Terrifying Blast', 'Situational Awareness',
                  'Sustained Determination']

revelations = ['Black Hole', 'Supernova', 'Constructive Interference', 'Dark Matter', 'Flare', 'Gravity Anchor',
               'Gravity Boost', 'Gravity Hold', 'Plasma Sheath', 'Radiation', 'Stellar Equilibrium', 'Stellar Rush',
               'Astrological Sense', 'Attactive Force', 'Blazing Orbit', 'Corona', 'Crush', 'Defy Gravity',
               'Glow of Life', 'Gravity Surge', 'Hypnotic Glow', 'Reflection', 'Subduing Beams', 'Burn Enchantment',
               'Debris Field', 'Soul Furnace', 'Stealth Warp', 'Gravity Shield', 'Particle Field',
               'Solar Fortification', 'Sunbolt', 'Ultimate Graviton', 'Ultimate Photon', 'Miniature Star',
               'Particle Wave', 'Quantum Entrapment', 'Ray of Light', 'Solar Acceleration', 'Starquake',
               'Time Dilation', 'Wormholes']

hacks = ['Countertech', 'Empowered Weapon', 'Energize Spell', 'Fabricate Tech', 'Harmful Spells', 'Quick Scan',
         'Recode Gem', 'Robot Influence', 'Selective Targeting', 'Spell Countermeasures', 'Summon Cache',
         'Technomantic Proficiency', 'Charging Jolt', 'Debug Spell', 'Distant Spell', 'Enchanted Fusion',
         'Extended Spell', 'Fabricate Arms', 'Magic Negation', 'Spell Grenade', 'Diviner\'s Tap',
         'Fabricate Explosive', 'Flash Teleport', 'Mental Mark', 'Spellshot', 'Tech Countermeasures', 'Widened Spell',
         'Countertech Sentinel', 'Eternal Spell', 'Reboot Mind', 'Seeking Shot', 'Phase Shot', 'Quickened Spell',
         'Rain of Fire', 'Spell Library']

tspells1 = ['Baleful Polymorph', 'Comprehend Languages', 'Detect Radiation', 'Detect Tech', 'Disguise Self', 'Erase',
            'Flight', 'Gloom Mote', 'Grease', 'Hold Portal', 'Holographic Image', 'Identify', 'Incompetence',
            'Jolting Surge', 'Junk Armor', 'Junk Sword', 'Keen Senses', 'Life Bubble', 'Magic Missile',
            'Necromantic Revitalization', 'Overheat', 'Polymorph', 'Summon Creature', 'Supercharge Weapon',
            'Unseen Servant']

tspells2 = ['Augury', 'Baleful Polymorph', 'Command Undead', 'Darkvision', 'Daze Monster', 'Emberstep', 'Fear',
            'Fog Cloud', 'Force Blast', 'Hold Person', 'Hurl Forcedisk', 'Inflict Pain', 'Mind Thrust', 'Mystic Cure',
            'Necromantic Revitalization', 'Paranoia', 'Polymorph', 'Reject Augmentation', 'Remove Condition',
            'Restoration (Lesser)', 'See Invisibility', 'Shield Other', 'Spider Climb', 'Status', 'Summon Creature',
            'Zone of Truth']

tspells3 = ['Baleful Polymorph', 'Bestow Curse', 'Burning Ash Clouds', 'Charm Monster', 'Clairaudience/Clairvoyance',
            'Deep Slumber', 'Dispel Magic', 'Fear', 'Haste', 'Hologram Memory', 'Irradiate', 'Mental Block',
            'Mind Thrust', 'Mystic Cure', 'Necromantic Revitalization', 'Nightmare', 'Polymorph',
            'Psychokinetic Strangulation', 'Ray of Exhaustion', 'Remove Affliction', 'Resistant Armor (Lesser)',
            'Slow', 'Speak with Dead', 'Suggestion', 'Summon Creature', 'Synaptic Pulse', 'Tongues',
            'Umbral Tendril', 'Viral Destruction']

tspells4 = ['Animate Dead', 'Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Borrow Corruption', 'Confusion',
            'Control Atmosphere', 'Cosmic Eddy', 'Death Ward', 'Dimensional Anchor', 'Discern Lies', 'Dismissal',
            'Divination', 'Enervation', 'Fear', 'Hold Monster', 'Mind Probe', 'Mind Thrust', 'Mystic Cure',
            'Necromantic Revitalization', 'Planar Binding', 'Polymorph (Mass)', 'Polymorph', 'Read the Flames',
            'Reincarnate', 'Remove Radioactivity', 'Resistant Armor', 'Restoration', 'Shadow Jump', 'Summon Creature',
            'Telepathic Bond']

tspells5 = ['Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Battlemind Link', 'Break Enchantment', 'Call Cosmos',
            'Command (Greater)', 'Commune With Nature', 'Contact Other Plane', 'Crush Skull', 'Dismissal',
            'Dispel Magic (Greater)', 'Dominate Person', 'Feeblemind', 'Mind Thrust', 'Modify Memory',
            'Mystic Cure (Mass)', 'Necromantic Revitalization', 'Planar Binding', 'Polymorph (Mass)', 'Polymorph',
            'Raise Dead', 'Reanimate', 'Remove Condition (Greater)', 'Resistant Aegis', 'Retrocognition',
            'Shadow Body', 'Summon Creature', 'Synaptic Pulse (Greater)', 'Telepathy', 'Waves of Fatigue']

tspells6 = ['Baleful Polymorph', 'Baleful Polymorph (Mass)', 'Control Gravity', 'Control Undead', 'Enshrining Refuge',
            'Ethereal Jaunt', 'Flesh to Stone', 'Gravitational Singularity', 'Inflict Pain (Mass)', 'Mind Swap',
            'Mind Thrust', 'Mystic Cure (Mass)', 'Mystic Cure', 'Necromantic Revitalization', 'Planar Barrier',
            'Planar Binding', 'Plane Shift', 'Polymorph (Mass)', 'Psychic Surgery', 'Regenerate',
            'Resistant Armor (Greater)', 'Shadow Walk', 'Snuff Life', 'Subjective Relative', 'Suggestion (Mass)',
            'Summon Creature', 'Telepathic Jaunt', 'True Seeing', 'Vision']


def character_generator():
    character = {}

    character_race = random.choice(races)
    character['Race'] = character_race

    character_gender = random.choice(['M', 'F', 'A'])
    character['Gender'] = character_gender

    if character_race != 'Android':
        age = random.choice(range(18, 60))
        character['Age'] = str(age)
    else:
        character['Age'] = 'N/A'

    character_class = random.choice(classes)
    character['Class'] = character_class

    if character_class == 'Mystic':
        mystic_connection = random.choice(connections)
        character['Conn.'] = mystic_connection

        character_spells = set()
        spell_1 = random.choice(mspells1)

        character_spells.add(spell_1)

        spell_2 = random.choice(mspells2)
        if spell_1 == spell_2:
            while spell_1 == spell_2:
                spell_2 = random.choice(mspells2)
        character_spells.add(spell_2)

        spell_3 = random.choice(mspells3)
        if spell_1 == spell_3 or spell_2 == spell_3:
            while spell_1 == spell_3 or spell_2 == spell_3:
                spell_3 = random.choice(mspells3)
        character_spells.add(spell_3)

        spell_4 = random.choice(mspells4)
        if spell_1 == spell_4 or spell_2 == spell_4 or spell_3 == spell_4:
            while spell_1 == spell_4 or spell_2 == spell_4 or spell_3 == spell_4:
                spell_4 = random.choice(mspells4)
        character_spells.add(spell_4)

        spell_5 = random.choice(mspells5)
        if spell_1 == spell_5 or spell_2 == spell_5 or spell_3 == spell_5 or spell_4 == spell_5:
            while spell_1 == spell_5 or spell_2 == spell_5 or spell_3 == spell_5 or spell_4 == spell_5:
                spell_5 = random.choice(mspells5)
        character_spells.add(spell_5)

        spell_6 = random.choice(mspells6)
        if spell_1 == spell_6 or spell_2 == spell_6 or spell_3 == spell_6 or spell_4 == spell_6 or spell_5 == spell_6:
            while spell_1 == spell_6 or spell_2 == spell_6 or spell_3 == spell_6 or spell_4 == spell_6 or spell_5 == spell_6:
                spell_6 = random.choice(mspells6)
        character_spells.add(spell_6)

        spells_chain = ''
        for pos, x in enumerate(character_spells):
            x.split(' ')
            if pos == 5:
                spells_chain += x
            else:
                spells_chain += x + ', '
        character['Spells'] = spells_chain

    elif character_class == 'Operative':
        operative_specialization = random.choice(specializations)
        character['Spec.'] = operative_specialization
        character_exploits = set()
        trigger = True
        while trigger:
            character_exploits.add(random.choice(exploits))
            if len(character_exploits) == 6:
                trigger = False
        exploits_chain = ''
        for pos, x in enumerate(character_exploits):
            x.split(' ')
            if pos == 5:
                exploits_chain += x
            else:
                exploits_chain += x + ', '
        character['Exploits'] = exploits_chain

    elif character_class == 'Soldier':
        fighting_style = random.choice(fighting_styles)
        character['F. Style'] = fighting_style
        character_boosts = set()
        trigger = True
        while trigger:
            character_boosts.add(random.choice(boosts))
            if len(character_boosts) == 2:
                trigger = False
        boosts_chain = ''
        for pos, x in enumerate(character_boosts):
            x.split(' ')
            if pos == 1:
                boosts_chain += x
            else:
                boosts_chain += x + ', '
        character['Gear Boosts'] = boosts_chain

    elif character_class == 'Mechanic':
        ai = random.choice(ais)
        character['A.I.'] = ai
        character_tricks = set()
        trigger = True
        while trigger:
            character_tricks.add(random.choice(tricks))
            if len(character_tricks) == 6:
                trigger = False
        tricks_chain = ''
        for pos, x in enumerate(character_tricks):
            x.split(' ')
            if pos == 5:
                tricks_chain += x
            else:
                tricks_chain += x + ', '
        character['Tricks'] = tricks_chain

    elif character_class == 'Solarian':
        character['Manifestation'] = random.choice(['Solar Weapon', 'Solar Armor'])
        character_revelations = set()
        trigger = True
        while trigger:
            character_revelations.add(random.choice(revelations))
            if len(character_revelations) == 5:
                trigger = False
        revelations_chain = ''
        for pos, x in enumerate(character_revelations):
            x.split(' ')
            if pos == 4:
                revelations_chain += x
            else:
                revelations_chain += x + ', '
        character['Revelations'] = revelations_chain

    elif character_class == 'Technomancer':
        character_hacks = set()
        trigger = True
        while trigger:
            character_hacks.add(random.choice(hacks))
            if len(character_hacks) == 5:
                trigger = False
        hacks_chain = ''
        for pos, x in enumerate(character_hacks):
            x.split(' ')
            if pos == 4:
                hacks_chain += x
            else:
                hacks_chain += x + ', '
        character['Magic Hacks'] = hacks_chain

    character_skills = set()
    trigger = True
    while trigger:
        character_skills.add(random.choice(skills))
        if len(character_skills) == 5:
            trigger = False
    skills_chain = ''
    for pos, x in enumerate(character_skills):
        x.split(' ')
        if pos == 4:
            skills_chain += x
        else:
            skills_chain += x + ', '
    character['Skills'] = skills_chain

    if character_class == 'Envoy':
        expertises = []
        for skill in character_skills:
            if skill == 'Disguise':
                expertise_talent = random.choice(['Altered Bearing', 'Borrowed Guise', 'Cunning Disguise'])
                expertises.append(expertise_talent)
            elif skill == 'Sense Motive':
                expertise_talent = random.choice(['Analyst', 'Keen Observer'])
                expertises.append(expertise_talent)
            elif skill == 'Medicine':
                expertise_talent = random.choice(['Battlefield Medic', 'Inspired Medic', 'Surgeon'])
                expertises.append(expertise_talent)
            elif skill == 'Computers':
                expertise_talent = random.choice(['Computer Whiz', 'Expert Forger', 'Fast Hack'])
                expertises.append(expertise_talent)
            elif skill == 'Bluff':
                expertise_talent = random.choice(['Convincing Liar', 'Create Diversion'])
                expertises.append(expertise_talent)
            elif skill == 'Culture':
                expertise_talent = random.choice(['Cultural Savant', 'Skilled Linguist', 'Tech Familiarity'])
                expertises.append(expertise_talent)
            elif skill == 'Engineering':
                expertise_talent = random.choice(['Demolition Expert', 'Engineering Adept', 'Student of Technology'])
                expertises.append(expertise_talent)
            elif skill == 'Intimidate':
                expertise_talent = random.choice(['Menacing Gaze', 'Rattling Presence'])
                expertises.append(expertise_talent)
            elif skill == 'Diplomacy':
                expertise_talent = random.choice(['Slick Customer', 'Well Informed'])
                expertises.append(expertise_talent)

        expertise_chain = ''
        for pos, x in enumerate(expertises):
            x.split(' ')
            expertise_chain += x + ', '
        if expertise_chain[-1] == ' ':
            correct_expertise_chain = expertise_chain[:-2]
            character['Exp.T.'] = correct_expertise_chain
        else:
            character['Exp.T.'] = expertise_chain

        character_improvs = set()
        trigger = True
        while trigger:
            character_improvs.add(random.choice(improvisations))
            if len(character_improvs) == 4:
                trigger = False
        improvs_chain = ''
        for pos, x in enumerate(character_improvs):
            x.split(' ')
            if pos == 3:
                improvs_chain += x
            else:
                improvs_chain += x + ', '
        character['Improvisations'] = improvs_chain

    character_theme = random.choice(themes)
    character['Theme'] = character_theme

    return character


def table_printer(dictionary):
    longest_item = 0
    for item in dictionary.items():
        if len(item[1]) > longest_item:
            longest_item = len(item[1])
    print('='.center((longest_item // 2) + longest_item, '='))
    for item, value in dictionary.items():
        print(item.ljust(longest_item // 2) + value.ljust(longest_item // 2))
    return '='.center((longest_item // 2) + longest_item, '=')


print(table_printer(character_generator()))
