import json

from aiohttp import ClientSession
from aiofiles import os, open
from nonebot_plugin_nps.consts import DATA_DIR, INDEX_PATH, SOURCE_PATH
from nonebot.log import logger
from nonebot.plugin import load_plugin
from pydantic import parse_obj_as

from nonebot_plugin_nps.fetch import fetch_online_plugins_from_all_sources

from nonebot_plugin_nps.local import get_should_load_plugins_name


async def init():
    logger.info("Init NoneBot Plugin Store")
    await check_and_create_dir()
    await load_plugins()


async def check_and_create_dir():
    """
    Check and create necessary directories
    Returns:
    """
    if not await os.path.exists(DATA_DIR):
        logger.info(f"Create data directory: {DATA_DIR}")
        await os.makedirs(DATA_DIR)

    if not await os.path.exists(SOURCE_PATH):
        # plugins.json
        logger.info(f"Create source directory: {SOURCE_PATH}")
        async with open(SOURCE_PATH, 'w', encoding="utf-8") as f:
            async with ClientSession() as session:
                plugins, err = await fetch_online_plugins_from_all_sources(session)
                if err:
                    logger.error(f"Failed to fetch plugins: {err}")
                    return
                await f.write(
                    json.dumps(
                        [plugin.dict() for plugin in plugins],
                        ensure_ascii=False,
                        indent=4
                    )
                )

    if not await os.path.exists(INDEX_PATH):
        # index.json
        logger.info(f"Create index directory: {INDEX_PATH}")
        async with open(INDEX_PATH, 'w', encoding="utf-8") as f:
            await f.write(json.dumps([], ensure_ascii=False, indent=4))


async def load_plugins():
    logger.info("Loading plugins by nonebot_plugin_nps")
    plugin_names, err = await get_should_load_plugins_name()
    if err:
        logger.error(f"Failed to load plugins: {err}")
        return
    for plugin_name in plugin_names:
        load_plugin(plugin_name)
