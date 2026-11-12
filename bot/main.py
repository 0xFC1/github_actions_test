import logging
import os

from aiogram import Bot, Dispatcher, F, types

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


async def start_command(message: types.Message) -> None:
    await message.answer("Привет! Я бот. Нажми /start, чтобы начать.")


def main() -> None:
    if BOT_TOKEN is None:
        raise RuntimeError("BOT_TOKEN environment variable is not set")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(start_command, F.command.text == "/start")

    dp.run_polling(bot)


if __name__ == "__main__":
    main()
