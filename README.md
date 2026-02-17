# Telegram AI Assistant Model

This repository contains the source code for an asynchronous Telegram bot model powered by the Gemini 2.5 Flash AI engine. This is a modular framework designed for personal use and technical demonstration.

## Mandatory Configuration
This project is not a standalone executable. It requires a manual setup of a configuration file to function correctly. Users must provide their own API tokens and access IDs.

### How to Set Up the Configuration File
1. Create a new file named `config.py` in the root directory of the project.
2. Add the following variables to `config.py`:
   - `TOKEN`: Your unique Telegram Bot Token from BotFather.
   - `CHAT_ID`: Your specific numeric Telegram user ID to restrict access to the owner only.
   - `GEMINI_API_KEY`: Your personal key obtained from Google AI Studio.
3. The `.gitignore` file is pre-configured to exclude `config.py` from being uploaded to public repositories to ensure your credentials remain private.

## Technical Features
* Asynchronous Operation: Utilizes the aiogram 3.x framework for non-blocking message handling.
* AI Character Control: Includes system instructions to ensure the model communicates in a concise, friendly, and accurate manner.
* Output Filtering: Automatically strips Markdown formatting such as asterisks and underscores to provide a clean, plain-text experience in the Telegram interface.
* Memory Management: Includes a /reset command that reinitializes the AI chat session, clearing all previous context.

## Installation Requirements
- Python 3.12 or higher.
- Dependencies listed in `requirements.txt`.
- Install all necessary packages, including aiogram and google-genai, using the provided manifest: `pip install -r requirements.txt`
- Install only when you are in .venv
- An active Linux or Ubuntu environment for stable execution.

## Usage and Troubleshooting
- To start the bot, run `python3 aiassistant.py`.
- If the bot returns an Error 429, it indicates that the current Google API quota has been exhausted for the day.
- The bot includes a security filter that verifies the sender's ID against the configured `CHAT_ID` before processing any request.