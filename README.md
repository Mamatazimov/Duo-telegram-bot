# Project: Telegram Online Theater Bot

This project is a public Telegram bot developed using Python's [aiogram](https://github.com/aiogram/aiogram) library. The primary goal of this bot is to create a small online theater focused on anime and manga content. Users can browse and watch videos directly through the bot.

The bot utilizes Telegram's servers for video storage and manages video playback using their unique file IDs. Additionally, a key learning experience from this project was working dynamically with inline buttons.

## Features

- Video storage and retrieval using Telegram's server
- Dynamic inline button interactions
- SQLite3 database integration for user and content management
- Aiogram-based command handling

## Installation

1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Set up your Telegram bot token:
   - Obtain a bot token from [BotFather](https://t.me/BotFather)
   - Configure your environment to store the token securely.

## Usage

Run the bot using:
```sh
python bot.py
```
The bot will allow users to browse and watch videos through inline button interactions.

## License

This project is open-source and available for public use under the MIT License.

