from pydantic import BaseModel


class Source(BaseModel):
    name: str
    url: str


class PluginTag(BaseModel):
    label: str
    color: str


class Plugin(BaseModel):
    module_name: str  # 模块名
    project_link: str  # 项目链接
    name: str  # 插件名
    desc: str  # 插件描述
    author: str  # 作者
    homepage: str  # 主页
    tags: list[PluginTag]  # 标签
    is_official: bool  # 是否官方插件
    type: str | None  # 类型
    supported_adapters: list[str] | None  # 支持的适配器
    valid: bool  # 是否有效
    version: str  # 版本
    time: str  # 时间
    skip_test: bool  # 是否跳过测试

    source: str = ""  # 源，手动添加
