import random

class player:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.mana = 20
        self.max_mana = 20
        self.damage = 2

    def set_hp(self,hp):
        self.hp = hp
    def set_max_hp(self,max_hp):
        self.max_hp = max_hp
    def set_mana(self,mana):
        self.mana = mana
    def max_max_mana(self, max_mana):
        self.max_mana = max_mana

    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.max_hp
    def get_mana(self):
        return self.mana
    def get_max_mana(self):
        return self.max_mana
