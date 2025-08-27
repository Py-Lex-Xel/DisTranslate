# DisTranslate

[🇷🇺 Русская версия](README.md)

A simple Discord bot for translating messages into different languages.  
Built with [disnake](https://github.com/DisnakeDev/disnake) and [googletrans](https://pypi.org/project/googletrans/).

## ✨ Features
- Translate text or message by ID / link to a specified language
- Supports slash commands
- Nice display using Embed
- `/invite` command to invite the bot to another server

## 🚀 Installation and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Py-Lex-Xel/DisTranslate.git
   cd DisTranslate
   ```

2. Install dependencies:
   ```bash
   pip install disnake googletrans==4.0.0-rc1
   ```

3. In `bot.py` replace:
   ```python
   bot.run("Token")
   ```
   with your Discord Bot Token.

4. Run the bot:
   ```bash
   python bot.py
   ```

## ▶️ Usage
- `/translator <text or message ID or link> <language code>`  
  Example:  
  ```bash
  /translator Hello ru
  ```
  Response will be an embed with the original text and translation.

- `/invite`  
  Sends an invite link to add the bot to another server.

## ⚙️ Requirements
- Python 3.9+
- `disnake`
- `googletrans`

## 📝 Notes
- Translation uses `googletrans`, which relies on an unofficial Google Translate API. Errors or limitations may occur.
- Educational project: minimal logic, but functional Discord translator.

## 📄 License
Free to use for personal and educational purposes.
