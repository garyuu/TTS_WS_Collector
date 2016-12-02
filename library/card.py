"""
==============================
@ Card
==============================
Date: 2016/11/30
Creator: Garyuu
Usage: Saving card information
==============================
"""

class Card:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.rarity = ""
        self.side = ""
        self.expansion = ""
        self.type = ""
        self.color = ""
        self.level = 0
        self.cost = 0
        self.power = 0
        self.soul = 0
        self.trigger = False
        self.attribute = []
        self.text = ""
        self.flavor = ""
        self.illustrator = ""
