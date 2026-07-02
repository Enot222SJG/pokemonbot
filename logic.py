from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.defense = self.get_defense()
        self.type = self.get_type()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][0]['base_stat']
        else:
            return 50

    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][1]['base_stat']
        else:
            return 50

    def get_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][2]['base_stat']
        else:
            return 50

    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['types'][0]['type']['name']
        else:
            return "normal"

    def info(self):
        return (f"Имя твоего покемона: {self.name}\n"
                f"Тип: {self.type}\n"
                f"HP: {self.hp}\n"
                f"Атака: {self.attack}\n"
                f"Защита: {self.defense}")

    def show_img(self):
        return self.img

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_attack(self, new_attack):
        self.attack = new_attack

    def set_defense(self, new_defense):
        self.defense = new_defense

    def set_type(self, new_type):
        self.type = new_type
