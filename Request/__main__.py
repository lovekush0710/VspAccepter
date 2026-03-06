import asyncio
import importlib
from config import START_IMG,OWNER_ID
from pyrogram import idle

from Request import LOGGER, Mukesh
from Request.modules import ALL_MODULES


async def _start():
    try:
        await Mukesh.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Request.modules." + all_module)

    LOGGER.info(f"@{Mukesh.username} Started.")
    await Mukesh.send_photo(8279029904,START_IMG,"❤️I am Alive boss❤️")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(_start())
    LOGGER.info("Stopping  bot")
