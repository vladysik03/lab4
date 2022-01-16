class Machine:
    level = 1

    def __init__(self):
        self.hp = 100
        self.damage = 30
        self.aggression = 70

    def attack(self):
        print('Attack!')
        return self.damage

    def loot(self):
        return None

    def get_damage(self, damage):
        self.hp -= damage
        self.newattr = 99

    def __repr__(self):
        return f'Machine:\n hp: {self.hp} \n damage: {self.damage}'

    def __gt__(self, other):
        print('In gt')
        if self.hp > other.hp:
            return True
        return False

    def __reduce_aggression(self):
        print("I'm calm")


class TerraformMachine:
    head_implant = 'implant'

    def __init__(self):
        pass

    def dig_soil(self):
        print('Hello Terraform')


class Strider(Machine, TerraformMachine):

    def __init__(self):
        Machine.__init__(self)
        TerraformMachine.__init__(self)
        self.hp = self.hp + 100
        self.objects = ['Blaze']

    def loot(self):
        s = Machine.loot(self)
        self.objects.append(s)
        return self.objects


machine_first = Machine()
machine_second = Machine()
strider_first = Strider()
strider_first.attack()
print(strider_first.loot())

print(strider_first.head_implant)


l = [machine_first, machine_second, strider_first]

for machine in l:
    print(machine.loot())



machine_first.hp += 5
res = machine_first > machine_second
print(res)
machine_first.attack()
Machine.attack(machine_first)
machine_first._Machine__reduce_aggression()
machine_first.damage = 35
