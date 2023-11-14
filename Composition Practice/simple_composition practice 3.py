# Define a class for the Weapon
class Weapon:
    def __init__(self, name, damage):
        self.weapon_name = name
        self.damage = damage

# Define a class for the Player
class Player:
    def __init__(self, id, name, mail, city, weapon):
        # Initialize basic player attributes
        self.id = id
        self.name = name
        self.mail = mail
        self.city = city
        # Use composition to include a Weapon object as part of the Player
        self._weapon = weapon  # The underscore (_) conventionally indicates a "protected" variable

    def attack(self):
        # Display a message about the player's attack using their weapon
        print(f'Player {self.name} attacks with {self._weapon.weapon_name}')
        print()

    def display_info(self):
        # Display detailed information about the player and their weapon
        print(f'Player ID: {self.id}')
        print(f'Player Name: {self.name}')
        print(f'Player Email: {self.mail}')
        print(f'Player City: {self.city}')
        print(f'Player Weapon Name: {self._weapon.weapon_name}')
        print(f'Player Weapon Damage: {self._weapon.damage}')
        print()

# Create instances of the Weapon class
ak47 = Weapon('AK 47', 1000)
m416 = Weapon('M 416', 975)

# Create instances of the Player class, each with a different weapon
p1 = Player(1, 'James Bond', 'james.bond@gmail.com', 'New York', weapon=ak47)
p2 = Player(2, 'Melana Henary', 'melana.h3167@gmail.com', 'Mexico', weapon=m416)

# Demonstrate attacks and display player information
p1.attack()
p1.display_info()

print('----------------------')

p2.attack()
p2.display_info()
