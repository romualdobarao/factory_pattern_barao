#we define an Enemy base class with properties like name, strength, speed, and attack_power, and a common attack method that prints a message to the console.
class Enemy:
    def __init__(self, name, strength, speed, attack_power):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power.")
#Then we define three subclasses of Enemy, namely Goblin, Orc, and Troll, that inherit from the base class and set their unique attributes in their constructors
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 10, 5, 2)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 15, 3, 3)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 20, 2, 5)
#we define an EnemyFactory class that has a create_enemy method that takes an enemy_type string and returns an instance of the corresponding enemy class
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
#We create an instance of the factory class and use it to create instances of the specific enemy types.
enemy_factory = EnemyFactory()
goblin = enemy_factory.create_enemy("Goblin")
orc = enemy_factory.create_enemy("Orc")
troll = enemy_factory.create_enemy("Troll")
#When we call the attack method on the enemy instances, it prints the appropriate message to the console based on the attack_power attribute of the instance.
goblin.attack()
orc.attack()
troll.attack()
