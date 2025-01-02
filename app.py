import json
import random

# Load data from the JSON file
with open("Characters.json", encoding="utf8") as test:
    data = json.load(test)

# Character class
class Character:
    def __init__(self, name, health, punch_damage, kick_damage, ultimate_attack, ultimate_attack_2_0):
        self.name = name
        self.health = health
        self.punch_damage = punch_damage
        self.kick_damage = kick_damage
        self.ultimate_attack = ultimate_attack
        self.ultimate_attack_2_0 = ultimate_attack_2_0

    # Method for attacking the opponent
    def attack(self, opponent, attack_type):
        if attack_type == 'punch':
            damage = self.punch_damage
            print(f"{self.name} punches {opponent.name} and deals {damage} damage!")
        elif attack_type == 'kick':
            damage = self.kick_damage
            print(f"{self.name} kicks {opponent.name} and deals {damage} damage!")
        elif attack_type == 'ultimate':
            damage = self.ultimate_attack
            print(f"{self.name} uses {self.ultimate_attack_2_0} and deals {damage} damage!")
        else:
            damage = 0
            print(f"{self.name} misses the attack!")

        opponent.health -= damage  # Reduce the opponent's health by the damage

    # Method to check if the character is still alive
    def is_alive(self):
        return self.health > 0

    def choose_attack(self):
        # Let the user choose an attack
        print(f"\n{self.name}'s turn:")
        print("Choose your attack:")
        print("1. Punch")
        print("2. Kick")
        print("3. Ultimate Attack (Super Duper!)")
        print("4. Ultimate Attack 2.0")
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == '1':
            return 'punch'
        elif choice == '2':
            return 'kick'
        elif choice == '3':
            return 'ultimate'
        elif choice == '4':
            return 'ultimate_2_0'
        else:
            print("Invalid choice! You missed your turn!")
            return 'miss'

# Create hero and villain objects using data from the JSON
hero_data = data['characters'][0]  # Stella (first hero in the JSON)
villain_data = data['characters'][2]  # OG (villain in the JSON)

hero = Character(hero_data['name'], hero_data['hp'], 
                 hero_data['basic_attack_damage_punch'], hero_data['basic_attack_damage_kick'], 
                 hero_data['ultimate_attack_super_duper_stella'], 
                 hero_data['ultimate_attack_super_duper_stella_2_0'])

villain = Character(villain_data['name'], villain_data['hp'], 
                    villain_data['basic_attack_damage_punch'], villain_data['basic_attack_damage_kick'], 
                    villain_data['ultimate_attack_super_duper_og'], 
                    villain_data['ultimate_attack_super_duper_og_2_0'])

# The fight loop (Player vs. Villain)
while hero.is_alive() and villain.is_alive():
    # Hero's turn
    attack_choice = hero.choose_attack()
    hero.attack(villain, attack_choice)
    print(f"Villain's health: {villain.health}")

    if not villain.is_alive():
        break

    # Villain's turn (AI chooses randomly)
    attack_choice = random.choice(['punch', 'kick', 'ultimate'])
    print(f"\n{villain.name} attacks (AI) with {attack_choice}!")
    villain.attack(hero, attack_choice)
    print(f"Hero's health: {hero.health}\n")

# Decide who won
if hero.is_alive():
    print("The Brave Hero won the fight!")
else:
    print("The Evil Villain won the fight!")
