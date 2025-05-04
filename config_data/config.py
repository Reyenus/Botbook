from dataclasses import dataclass
from environs import Env


@dataclass
class Tgbot:
    token: str
    admin_id: list[int]


@dataclass
class Config:
    tg_bot: Tgbot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=Tgbot(
            token=env("BOT_TOKEN"), admin_id=list(map(int, env.list("ADMIN_ID")))
        )
    )

