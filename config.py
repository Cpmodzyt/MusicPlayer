"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "28889770")
        self.API_HASH: str = os.environ.get("API_HASH", "0ecaead60f942ee1c8415bcb336e7329")
        self.SESSION: str = os.environ.get("SESSION", "BQG40qoAaBiB8o2t-0tA2wtXT2vxhvIwKv3yxWC_4sdS06npatNzW8fNwtwL7cQhh_8WZkPvuPiMywvIlmd_YF4IrtLpfomgAO5dvsQa2jgAehct65FgmZ-fcHwDpXtYD-kSWDlgDwwgHMGILza7v0BSavDMQeSa_oCPKqSqgDpUjwFtAxvKgInXA34kbf-eXwKiiPZMiaNKEVQ0Q37tOmuyDK0rBs-vrSxJMAaiDtbmhfciXdCRIJggSAJ5mKSzlsdXX_GS7hm3SLrt-5FMgOKUrvg4_S11Iy-SDjIRcexjbp8lrQKVRuTva4qhKy-OG4I3SaD3RuqBoYJiX1gYaUGYPsNfdwAAAAHBc6w6AA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7701703310:AAGXi1-8_co_aI3yYljoGX_MZBRboQqtfFE")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "7717701360").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
