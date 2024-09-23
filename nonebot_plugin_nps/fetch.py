from aiohttp import ClientSession
from pydantic import parse_obj_as

from nonebot_plugin_nps.consts import INDEX_PATH, SOURCE_PATH
from nonebot_plugin_nps.models import Plugin
from nonebot_plugin_nps.sources import sources


async def fetch_online_plugins_from_all_sources(session: ClientSession) -> tuple[list[Plugin], Exception | None]:
    """
    Fetch plugins from all remote sources
    Returns:
        list[Plugin]: List of plugins
        err: Error
    """
    err = None
    plugins = []

    for source in sources:
        try:
            async with session.get(source.url) as resp:
                data = await resp.json()
                plugins.extend(data)
        except Exception as e:
            err = e
            break
    return parse_obj_as(list[Plugin], plugins), err


async def fetch_local_plugins() -> [list[Plugin], Exception | None]:
    """
    Fetch local plugins
    Returns:
        list[Plugin]: List of plugins
        err: Error
    """
    err = None
    plugins = []
    try:
        async with open(SOURCE_PATH, 'r', encoding="utf-8") as f:
            plugins = await f.json()
    except Exception as e:
        err = e
    return parse_obj_as(list[Plugin], plugins), err



