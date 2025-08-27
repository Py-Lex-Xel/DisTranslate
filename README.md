# DisTranslate

[🇷🇺 Русская версия](README.md) | [EN English version](README.en.md)

Простой Discord-бот для перевода сообщений на разные языки.  
Основан на [disnake](https://github.com/DisnakeDev/disnake) и [googletrans](https://pypi.org/project/googletrans/).

## ✨ Возможности
 1) Перевод текста или сообщения по ID / ссылке на указанный язык
 2) Поддержка slash-команд
 3) Красивый вывод через Embed
 4) Команда `/invite` для приглашения бота на другой сервер

## 🚀 Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Py-Lex-Xel/DisTranslate.git
   cd DisTranslate
   ```

2. Установите зависимости:
   ```bash
   pip install disnake googletrans==4.0.0-rc1
   ```

3. В файле `bot.py` замените:
   ```python
   bot.run("Token")
   ```
   на ваш Discord Bot Token.

4. Запустите бота:
   ```bash
   python bot.py
   ```

## ▶️ Использование
- `/translator <текст или ID сообщения или ссылка> <код языка>`  
  Пример:  
  ```bash
  /translator Hello ru
  ```
  Ответом будет embed с оригинальным текстом и переводом.

- `/invite`  
  Отправляет ссылку-приглашение для добавления бота на сервер.

## ⚙️ Требования
 Python 3.9+
 `disnake`
 `googletrans`

## 📝 Примечания
1) Перевод работает через библиотеку `googletrans`, которая использует неофициальный API Google Translate. Иногда могут возникать ошибки или ограничения.
2) Это учебный проект: минимальная логика, но рабочий переводчик для Discord.

## 📄 Лицензия
Свободное использование для личных и учебных целей.  
