import telebot
from config import token
from logic import Pokemon, Fighter, Wizard
from random import randint

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        choice = randint(1, 3)
        if choice == 1:
            pokemon = Wizard(username)
        elif choice == 2:
            pokemon = Fighter(username)
        else:
            pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        bot.send_message(message.chat.id, Pokemon.pokemons[username].info())
    else:
        bot.reply_to(message, "Сначала создай покемона через /go")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        attacker = message.from_user.username
        target = message.reply_to_message.from_user.username
        if attacker in Pokemon.pokemons and target in Pokemon.pokemons:
            my_pokemon = Pokemon.pokemons[attacker]
            enemy_pokemon = Pokemon.pokemons[target]
            result = my_pokemon.attack(enemy_pokemon)
            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "У одного из вас нет покемона. Сначала /go")
    else:
        bot.reply_to(message, "Ответь на сообщение тренера, чьего покемона хочешь атаковать")

@bot.message_handler(commands=['heal'])
def heal(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        result = Pokemon.pokemons[username].heal()
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "Сначала создай покемона через /go")

bot.infinity_polling(none_stop=True)
