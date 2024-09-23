from nonebot_plugin_nps.models import Source

sources: list[Source] = [
    Source(
        name="NoneBot2官方源",
        url="https://registry.nonebot.dev/plugins.json"
    ),
    # Source(
    #     name="轻雪源",
    #     url="https://bot.liteyuki.icu/plugins.json"
    # )
]
