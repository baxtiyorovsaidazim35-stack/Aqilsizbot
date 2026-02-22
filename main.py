import asyncio
from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from buttons import menu,
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alaykum aziz bolmagan mijoz {message .from_user.full_name} Aziz bolmagan mijoz sizga baribir yordam bermiman",reply_markup=menu)

@dp.callback_query()
async def ans(callback:CallbackQuery):
    if callback.data=="aqil1":
        await callback.answer()
        await callback.message.answer("Nima ishqildinki kayfiyating juda yamon")
    elif callback.data=="aqil2":
        await callback.answer()
        await callback.message.answer("Boladigan bolsa yahshi 😁")
    elif callback.data=="aqil3":
        await callback.answer()
        await callback.message.answer("Sen menga yoqyapsanda a 😒")
    elif callback.data=="aqil4":
        await callback.answer()
        await callback.message.answer("Sen ham menga yoqyapsan 😄 ")
    elif callback.data=="aqil5":
        await callback.answer()
        await callback.message.answer("Mayli 🥺")
    elif callback.data=="aqil6":
        await callback.answer()
        await callback.message.answer("Kerakmas 😡")
    elif callback.data=="aqil7":
        await callback.answer()
        await callback.message.answer("Kel nastrenyangni kotaramiz 😄")
    elif calback.data=="aqil8":
        await callback.answer()
        await callback.message.answer("Hechnarsa qilishin shart emas")



# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    print("Bot muvafaqatsiz otdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
