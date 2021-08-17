from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

# loop = asyncio.get_event_loop()
# Поток нам не нужен, т.к. он и так создается в диспатчере.
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

async def on_shutdown(dp):
    await bot.close()

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    from aiogram import executor
    from handers import dp
    executor.start_polling(dp, on_startup=send_to_admin, on_shutdown=on_shutdown)
