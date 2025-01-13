import json
import random
with open("Characters.json", encoding="utf8") as test:
    data = json.load(test)

class Character:
    def __init__(self, name, health, punch_damage, kick_damage, ultimate_attack, ultimate_attack_2_0):
        self.name = name
        self.health = health
        self.punch_damage = punch_damage
        self.kick_damage = kick_damage
        self.ultimate_attack = ultimate_attack
        self.ultimate_attack_2_0 = ultimate_attack_2_0
    PUNCH = 'punch'
    KICK = 'kick'
    ULTIMATE = 'ultimate'
    ULTIMATE_2_0 = 'ultimate_2_0'
    HEAL = 'heal'
    # how to cause damage towards the villains
    def attack(self, opponent, attack_type):
        if attack_type == self.PUNCH:
            damage = self.punch_damage
            print(f"{self.name} punches {opponent.name} and deals {damage} damage!")
        elif attack_type == self.KICK:
            damage = self.kick_damage
            print(f"{self.name} kicks {opponent.name} and deals {damage} damage!")
        elif attack_type == self.ULTIMATE:
            damage = self.ultimate_attack
            print(f"{self.name} uses {self.ultimate_attack} and deals {damage} damage!")
        elif attack_type == self.ULTIMATE_2_0:
            damage = self.ultimate_attack_2_0
            print(f"{self.name} uses {self.ultimate_attack_2_0} and deals {damage} damage!")
        elif attack_type == self.HEAL: #no damage,just heal, ur immortal :)
            damage = 0   
        else:
            damage = 0
            print(f"{self.name} misses the attack!")

        opponent.health -= damage  # bye bye oppnonent health
    # to be dead or not to be dead
    def is_alive(self):
        return self.health > 0

    def choose_attack(self):
        # player chooses the attack
        print(f"\n{self.name}'s turn:")
        print("Choose your attack:")
        print("1. Punch")
        print("2. Kick")
        print("3. Ultimate Attack (Super Duper!)")
        print("4. Ultimate Attack (Super Super!)")
        print("5. Heal")
        choice = input("Enter 1, 2, 3, 4, or 5: ")

        if choice == '1':
            return 'punch'
        elif choice == '2':
            return 'kick'
        elif choice == '3':
            return 'ultimate'
        elif choice == '4':
            return 'ultimate_2_0'
        elif choice == '5':
            return 'heal'
        else:
            print("Invalid choice! You missed your turn!")
            return 'miss'

    def heal(self, healing_amount):
        self.health += healing_amount
        if self.health > self.max_health:
            self.health = self.max_health    
    def choose_heal(self):
        print(f"\n{self.name}'s turn:")
        print("5. Heal")
        choice = input("Enter 5: ")

        if choice == '5':
            healing_amount = 20
            self.heal(healing_amount)
        else:
            print("Invalid choice! You missed your turn!")

# player chooses character
def choose_character():
    print("Choose your character:")
    heroes = [character for character in data['characters'] if character['type'] == 'hero']
    
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero['name']} (Health: {hero['hp']})")
    
    choice = int(input("Pick a number (1, 2, 3...): "))  # Player picks a number
    selected_hero = heroes[choice - 1] 

    # Print the selected hero data 
    print(f"Selected Hero: {selected_hero}")

    # Ensure the correct names for ultimate attacks
    ultimate_attack = selected_hero.get('ultimate_attack_super_duper_connie', 0)  # Correct field name
    ultimate_attack_2_0 = selected_hero.get('ultimate_attack_super_duper_connie_2_0', 0)  # Correct field name

    # Debug print the ultimate attack values
    print(f"Ultimate Attack (Super Duper!): {ultimate_attack}")
    print(f"Ultimate Attack (Super Super!): {ultimate_attack_2_0}")

    # completes the character
    return Character(
        selected_hero['name'], 
        selected_hero['hp'], 
        selected_hero['basic_attack_damage_punch'], 
        selected_hero['basic_attack_damage_kick'],
        ultimate_attack, 
        ultimate_attack_2_0
    )

# honestly i dont know if i want this part or just make it randomized 
def choose_villain():
    villains = [character for character in data['characters'] if character['type'] == 'villain']
    selected_villain = random.choice(villains)
    return Character(
        selected_villain['name'],
        selected_villain['hp'],
        selected_villain['basic_attack_damage_punch'],
        selected_villain['basic_attack_damage_kick'],
        selected_villain.get('ultimate_attack_super_duper_og', 0),
        selected_villain.get('ultimate_attack_super_duper_og_2_0', 0)
    )

print("CHOOSE YOUR HERO")
hero = choose_character()

villain = choose_villain()


# the fighting 
while hero.is_alive() and villain.is_alive():
    # Hero's turn
    attack_choice = hero.choose_attack()
    hero.attack(villain, attack_choice)
    print(f"Villain's health: {villain.health}")

    if not villain.is_alive():
        break

    # Villain's turn 
    attack_choice = random.choice(['punch', 'kick', 'ultimate'])
    print(f"\n{villain.name} attacks (AI) with {attack_choice}!")
    villain.attack(hero, attack_choice)
    print(f"Hero's health: {hero.health}\n")

# Winner
if hero.is_alive():
    print(f"{hero.name} won the fight!")
else:
    print(f"{villain.name} won the fight!")

