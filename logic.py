from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.data = self._fetch_data()
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(100, 200)
        self.power = randint(10, 30)
        self.type = self.get_type()
        self.wins = 0
        Pokemon.pokemons[pokemon_trainer] = self

    def _fetch_data(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def get_img(self):
        if self.data:
            return self.data['sprites']['front_default']
        return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    def get_name(self):
        if self.data:
            return self.data['forms'][0]['name']
        return "Pikachu"

    def get_type(self):
        if self.data:
            return self.data['types'][0]['type']['name']
        return "normal"

    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            self.wins += 1
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    def info(self):
        return (f"Имя: {self.name}\n"
                f"Тип: {self.type}\n"
                f"HP: {self.hp}\n"
                f"Сила: {self.power}\n"
                f"Побед: {self.wins}")

    def show_img(self):
        return self.img

    def heal(self):
        self.hp = randint(100, 200)
        return f"{self.name} восстановил здоровье!"


class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp = randint(80, 150)
        self.power = randint(20, 40)

    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "

    def info(self):
        return "У тебя покемон-боец\n" + super().info()


class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp = randint(120, 220)
        self.power = randint(8, 20)

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        return super().attack(enemy)

    def info(self):
        return "У тебя покемон-волшебник\n" + super().info()
