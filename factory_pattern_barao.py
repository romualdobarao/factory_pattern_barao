#define ug enemy na base class
class Enemy:
    def __init__(self, name, strength, speed, attack_power):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power.")
#define dayon ug tulo ma subclasses
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 10, 5, 2)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 15, 3, 3)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 20, 2, 5)
#define ug EnemyFactory na class
class EnemyFactory:
    def create_enemy(self, enemy_type):
        if enemy_type == "Goblin":
            return Goblin()
        elif enemy_type == "Orc":
            return Orc()
        elif enemy_type == "Troll":
            return Troll()
        else:
            raise ValueError(f"Unknown enemy type {enemy_type}.")
#mag create instance sa enemy factory na class
enemy_factory = EnemyFactory()
goblin = enemy_factory.create_enemy("Goblin")
orc = enemy_factory.create_enemy("Orc")
troll = enemy_factory.create_enemy("Troll")
#tawagon ang call na method
goblin.attack()
orc.attack()
troll.attack()
