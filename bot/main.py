import logging
import os
from aiogram.types import Message

from aiogram import Bot, Dispatcher, F, types

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()                        # [2]


@dp.message()                            # [3]
async def any_message(message: Message):
    await message.answer("Hello world!") # [6]

def main() -> None:
    if BOT_TOKEN is None:
        raise RuntimeError("BOT_TOKEN environment variable is not set")

    bot = Bot(token=BOT_TOKEN)
    
    dp.run_polling(bot)


if __name__ == "__main__":
    main()
