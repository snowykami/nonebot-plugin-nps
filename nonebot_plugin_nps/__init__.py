from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from nonebot_plugin_nps.on_plugin_load import init

__plugin_meta__ = PluginMetadata(
    name="NoneBot2插件商店",
    description="一个管理NoneBot2插件安装和卸载的插件，支持多源拉取",
    usage="",
)

driver = get_driver()


@driver.on_startup
async def main():
    await init()
