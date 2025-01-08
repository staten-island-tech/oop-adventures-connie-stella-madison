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

    # how to cause damage towards the villains
    def attack(self, opponent, attack_type):
        if attack_type == 'punch':
            damage = self.punch_damage
            print("{} punches {} and deals {} damage!".format(self.name, opponent.name, damage))
        elif attack_type == 'kick':
            damage = self.kick_damage
            print("{} kicks {} and deals {} damage!".format(self.name, opponent.name, damage))
        elif attack_type == 'ultimate':
            damage = self.ultimate_attack
            print("{} uses Ultimate Attack 1.0 and deals {} damage!".format(self.name, damage))
        elif attack_type == 'ultimate_2_0':  # Handle Ultimate Attack 2.0 separately
            damage = self.ultimate_attack_2_0
            print("{} uses Ultimate Attack 2.0 and deals {} damage!".format(self.name, damage))
        else:
            damage = 0
            print("{} misses the attack!".format(self.name))

        opponent.health -= damage  # Decrease opponent health by damage

    # to be dead or not to be dead
    def is_alive(self):
        return self.health > 0
    def choose_attack(self):
        print(f"\n{self.name}'s turn:")
        print("Choose your attack:")
        print("1. Punch")
        print("2. Kick")
        print("3. Ultimate Attack 1.0")
        print("4. Ultimate Attack 2.0")
        while True:
            choice = input("Enter 1, 2, 3, or 4: ")
    
            print(f"Player chose: {choice}")

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
    
    return Character(
        selected_hero['name'], 
        selected_hero['hp'], 
        selected_hero['basic_attack_damage_punch'], 
        selected_hero['basic_attack_damage_kick'],
        selected_hero['ultimate_attack_super_duper_stella'] if 'ultimate_attack_super_duper_stella' in selected_hero else 0, 
        selected_hero['ultimate_attack_super_duper_stella_2_0'] if 'ultimate_attack_super_duper_stella_2_0' in selected_hero else 0  
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

# """ def heal(self, healing_amount, healing_type="basic"):
#     if healing_type == "potion":
#         healing_amount = 50  # Example for potion healing
#     elif healing_type == "magic":
#         healing_amount = 100  # Example for magic healing
    
#     # Heal logic as before...
#  """