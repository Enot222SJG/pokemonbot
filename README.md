# 🐾 Pokemon Battle Bot — Telegram Bot

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![Telegram](https://img.shields.io/badge/telegram-bot-26A5E4?logo=telegram)
![PokeAPI](https://img.shields.io/badge/api-PokeAPI-EF5350?logo=api)

> **Telegram-бот для игры в покемонов с возможностью сражений, кормления и прокачки!**

---

## 📋 Команды

| Команда | Описание |
|---------|----------|
| `/go` | Создать нового покемона (случайный класс: обычный, боец или волшебник) |
| `/info` | Показать характеристики покемона |
| `/attack` | Атаковать покемона другого тренера (ответом на его сообщение) |
| `/feed` | Покормить покемона (восстанавливает HP, есть кулдаун) |
| `/heal` | Полное восстановление здоровья |

---

## 🎮 Геймплей

### 👤 Создание покемона
```
/go
```
Бот случайным образом выбирает покемона из PokeAPI (1–1000) и назначает ему один из классов:

- **Pokemon** 🟢 — обычный, сбалансированные характеристики
- **Fighter** 🔴 — больше силы, супер-атака с рандомным бустом
- **Wizard** 🔵 — больше HP, магический щит (шанс уклониться)

### ⚔️ Сражение
Ответьте на сообщение соперника командой:
```
/attack
```
- **Fighter** наносит супер-удар (+5..+15 к силе)
- **Wizard** может активировать щит (20% шанс) и уклониться от атаки

### 🍽️ Кормление
```
/feed
```
- Восстанавливает HP (интервал: 60 сек для обычных, 30 сек для Fighter)
- Wizard получает больше HP от кормления

---

## 🧬 Классы

```
Pokemon (родительский)
├── Fighter  — сила выше, интервал кормления короче
└── Wizard   — HP выше, восстановление от кормления сильнее
```

Каждый класс переопределяет методы:
- `attack()` — уникальная механика боя
- `info()` — вывод с указанием класса
- `feed()` — свои параметры кормления

---

## 🛠 Установка и запуск

```bash
git clone https://github.com/Enot222SJG/pokemonbot
cd pokemonbot
pip install pyTelegramBotAPI requests
```

Вставьте токен бота в `config.py`:
```python
token = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
```

Запустите:
```bash
python main.py
```

---

## 📚 Использованные технологии

- **[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)** — работа с Telegram Bot API
- **[PokeAPI](https://pokeapi.co/)** — получение данных о покемонах
- **datetime / timedelta** — система кулдауна кормления
- **Наследование и полиморфизм** — классы Pokemon, Fighter, Wizard

---

## 🔗 Ссылки

- GitHub: [Enot222SJG/pokemonbot](https://github.com/Enot222SJG/pokemonbot)
- PokeAPI: [https://pokeapi.co/](https://pokeapi.co/)
- Telegram Bot Father: [@BotFather](https://t.me/BotFather)

---

<div align="center">
  <i>Make your Pokemon strong and defeat all rivals! ⚡</i>
</div>
