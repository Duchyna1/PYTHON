class Stats:
    MINE = {
        'speed': [50, 30, 20, 10]
    }
    CONVEYOR = {
        'speed': [10, 6, 4, 2],
        'color': ['red', 'green', 'blue', 'gold']
    }


class Buildings:
    MINE = 'mine'
    CONVEYOR = 'conveyor'
    BASE = 'base'
    all = [MINE, CONVEYOR, BASE]


class Materials:
    STONE = 'stone'
    COAL = 'coal'
    IRON = 'iron'
    GOLD = 'gold'
    DIAMOND = 'diamond'
    all = [STONE, COAL, IRON, GOLD, DIAMOND]
    colors = {
        STONE: '#494949',
        COAL: '#202020',
        IRON: 'navajo white',
        GOLD: 'yellow',
        DIAMOND: 'light blue'
    }
