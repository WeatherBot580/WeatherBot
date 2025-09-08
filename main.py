import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import google.generativeai as genai

# Замените на ваш токен бота от BotFather
BOT_TOKEN = '7913072463:AAFyb5g5Wpr-vGvrEzvbTo7If-Qu3v98EIw'

# Замените на ваш API ключ от Google Generative AI (получите на https://aistudio.google.com/app/apikey)
GEMINI_API_KEY = 'AIzaSyBv9p9e9bYgqR4g5rghvVxKFdPgU4jULDg'

# Настройка Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')  # Используем Gemini 2.5 Flash

dp = Dispatcher()

@dp.message(Command('start'))
async def send_weather(message: types.Message):
    try:
        # Запрос к Gemini для прогноза погоды и совета
        prompt = "Дай текущий прогноз погоды в Kropyvnytskyi (Украина) на русском языке, включая температуру, описание, влажность и скорость ветра. Затем дай совет, как одеться на основе этой погоды."
        response = model.generate_content(prompt)
        
        if not response.text:
            await message.reply("Не удалось получить ответ от Gemini. Проверьте API ключ или модель.")
            return

        # Отправляем ответ
        await message.reply(response.text)

    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
