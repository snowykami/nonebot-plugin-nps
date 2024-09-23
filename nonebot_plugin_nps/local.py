import json

import aiofiles

from nonebot_plugin_nps.consts import INDEX_PATH


async def get_should_load_plugins_name() -> [list[str], Exception | None]:
    """
    Fetch plugins that should be loaded
    Returns:
        list[Plugin]: List of plugins
        err: Error
    """
    err = None
    plugin_names = []
    try:
        async with aiofiles.open(INDEX_PATH, 'r', encoding="utf-8") as f:
            plugin_names = json.loads(await f.read())
    except Exception as e:
        err = e
    return plugin_names, err


async def remove_plugin_from_index(plugin_name: str) -> Exception | None:
    """Remove plugin name from index.json
    Args:
        plugin_name: Plugin
    Returns:
    """

    plugins, err = await get_should_load_plugins_name()
    if err:
        return err
    if plugin_name not in plugins:
        return ValueError(f"Plugin {plugin_name} not exists in index.json")
    plugins.remove(plugin_name)
    try:
        async with open(INDEX_PATH, 'w', encoding="utf-8") as f:
            await f.write(json.dumps(plugins))
    except Exception as e:
        err = e
    return err


async def add_plugin_to_index(plugin_name: str) -> Exception | None:
    """
    Add plugin name to index.json
    Args:
        plugin_name: Plugin
    Returns:
    """

    plugins, err = await get_should_load_plugins_name()
    if err:
        return err
    if plugin_name in plugins:
        return ValueError(f"Plugin {plugin_name} already exists in index.json")
    plugins.append(plugin_name)
    try:
        async with open(INDEX_PATH, 'w', encoding="utf-8") as f:
            await f.write(json.dumps(plugins))
    except Exception as e:
        err = e
    return err

