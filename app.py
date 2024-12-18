# Character class
class Character:
    def __init__(self, name, health):
        self.name = name  # The character's name
        self.health = health  # The character's health

    # Method for attacking the opponent
    def attack(self, opponent):
        damage = 10  # Each attack deals 10 damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")
        opponent.health -= damage  # Reduce the opponent's health by the damage

    # Method to check if the character is still alive
    def is_alive(self):
        return self.health > 0

# Creating two characters: Hero and Villain
<<<<<<< Updated upstream:app.py
hero = Character("Brave Hero", 100)  # Hero starts with 100 health
villain = Character("Evil Villain", 100)  # Villain starts with 100 health
=======
hero = Character("Madison", 50)
hero = Character("Stella", 150)
hero = Character("Connie", 150)
villain = Character("OG", 2000)  # Villain starts with 100 health
>>>>>>> Stashed changes:inspiration.py

# The fight
while hero.is_alive() and villain.is_alive():
    hero.attack(villain)  # Hero attacks Villain
    if villain.is_alive():
        villain.attack(hero)  # Villain attacks Hero
    print(f"Hero's health: {hero.health} | Villain's health: {villain.health}\n")

# Decide who won
if hero.is_alive():
    print("The Brave Hero won the fight!")
else:
    print("The Evil Villain won the fight!")
