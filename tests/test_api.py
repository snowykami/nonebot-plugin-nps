import pytest
from aiohttp import ClientSession

from nonebot_plugin_nps.fetch import (
    fetch_local_plugins, fetch_online_plugins_from_all_sources
)


class TestFetch:
    @pytest.mark.asyncio
    async def test_fetch_online(self):
        async with ClientSession() as session:
            plugins, err = await fetch_online_plugins_from_all_sources(session)
            assert err is None
            assert len(plugins) > 0
            for p in plugins:
                print("PASS", p.name, p.version)

    @pytest.mark.asyncio
    async def test_fetch_local(self):
        plugins, err = await fetch_local_plugins()
        assert err is None
        assert len(plugins) > 0
        for p in plugins:
            print(p.name, p.version)
