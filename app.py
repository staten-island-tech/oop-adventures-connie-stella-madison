# Character class
import json 
with open("Characters.json", encoding="utf8") as test:
    data = json.load(test)

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
