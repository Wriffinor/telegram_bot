import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
from google import genai

from config import TOKEN, CHAT_ID, GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = 'gemini-2.5-flash'
chat_session = None

bot = Bot(token=TOKEN)
dp = Dispatcher()

SYSTEM_PROMPT = ( "You are a lively and accurate assistant. Communicate in a friendly and concise manner, avoiding cliches."
"Write exclusively in lowercase letters, except for the first letter of a sentence. Be accurate with facts."
"Do not use caps lock unless the context of the sentence requires it."
"Do not use any markup: no asterisks (**), underscores (__), or hash tags (#)."
"Your output is plain text. Use only standard punctuation: periods, commas, and hyphens, dashes if the sentence requires them." )

async def get_chat():
    global chat_session
    if chat_session is None:
        chat_session = client.aio.chats.create(model= MODEL_NAME, config={'system_instruction': SYSTEM_PROMPT})
    return chat_session

@dp.message(Command("reset"))
async def reset_handler(message: types.Message):
    global chat_session
    chat_session = client.aio.chats.create(model= MODEL_NAME, config={'system_instruction': SYSTEM_PROMPT})
    await message.answer("History has been cleaned")

@dp.message()
async def handle_any_message(message: types.Message):
    if int(message.from_user.id) != int(CHAT_ID):
        return

    chat = await get_chat()

    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        try:
            response = await chat.send_message(message.text)
            clean_text = response.text.replace("**", "").replace("__", "").replace("#", "")
            await message.answer(clean_text)
        except Exception as e:
            print(f"Error Gemini: {e}")
            await message.answer("Sorry for this trouble...")

async def main():
    await bot.send_message(CHAT_ID, "Welcome to AI assistant")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())