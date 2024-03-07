import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram import html
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import collback
import config
from handlers import router

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    dp.include_router(router)
    dp.callback_query.register(collback.navigation)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


@dp.message(F.photo)
async def handle_media(message: types.Message):
    media_type = "фото"
    media_id = message.photo[-1].file_id
    if message.from_user.username in config.admin:
        await message.reply(f"Принято {media_type} от пользователя {message.from_user.username}. "
                            f"ID вложения: {html.code(media_id)}", parse_mode=ParseMode.HTML)
    else:
        await message.reply("Вложение не обработано")


@dp.message(F.video)
async def handle_media(message: types.Message):
    media_type = "видео"
    media_id = message.video.file_id
    if message.from_user.username in config.admin:
        await message.reply(f"Принято {media_type} от пользователя {message.from_user.username}. "
                            f"ID вложения: {html.code(media_id)}", parse_mode=ParseMode.HTML)
    else:
        await message.reply("Вложение не обработано")


@dp.message(F.video_note)
async def handle_media(message: types.Message):
    media_type = "видеосообщение"
    media_id = message.video_note.file_id
    if message.from_user.username in config.admin:
        await message.reply(f"Принято {media_type} от пользователя {message.from_user.username}. "
                            f"ID вложения: {html.code(media_id)}", parse_mode=ParseMode.HTML)
    else:
        await message.reply("Вложение не обработано")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
