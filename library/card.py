"""
==============================
@ Card
==============================
Date: 2016/11/30
Creator: Garyuu
Usage: Saving card information
==============================
"""

from enum import Enum

class colorEnum(Enum):
    yellow = b'\xE9\xBB\x83'.decode('utf-8')
    green = b'\xE7\xB6\xA0'.decode('utf-8')
    red = b'\xE7\xB4\x85'.decode('utf-8')
    blue = b'\xE8\x97\x8D'.decode('utf-8')

class Card:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.rarity = ""
        self.side = ""
        self.expansion = ""
        self.type = ""
        self.color = ""
        self.level = ""
        self.cost = ""
        self.power = ""
        self.soul = 0
        self.trigger = 0
        self.attribute = []
        self.text = ""
        self.official_image = ""
        self.image = ""

    def title(self):
        output = ""
        output += "{}[{}] {}".format(self.id, colorEnum[self.color].value, self.name)
        output += " {}/{} {}/{}".format(self.level, self.cost, self.power, self.soul)
        return output

    def description(self):
        output = ""
        output += "[{}]-[{}] ".format(self.attribute[0], self.attribute[1])
        for t in self.text:
            output += t + ' '
        return output
