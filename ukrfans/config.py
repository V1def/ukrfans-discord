# Copyright © 2021-2022 V1def

# This file is part of Ukrfans: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# Ukrfans is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with Ukrfans. If not, see <https://www.gnu.org/licenses/>.

"""Config file."""

import os
from pathlib import Path

import disnake
import dotenv

# Loading .env file variables.
dotenv.load_dotenv(dotenv.find_dotenv())

# Discord bot token.
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
# Reconnecting bot.
BOT_RECONNECT: bool = (os.getenv('BOT_RECONNECT', 'false') == 'true')
# Discord bot intents.
BOT_INTENTS: disnake.Intents = disnake.Intents.all()

# Embed color.
EMBED_COLOR: int = 0x215AF4
# Error embed color.
EMBED_ERROR_COLOR: int = 0xFF0800

# Debug mode.
DEBUG: bool = (os.getenv('DEBUG', 'false') == 'true')

# Log file path.
LOG_FILE_PATH: Path = "ukrfans/ukrfans-log.log"
# Compression log file.
LOGGER_COMPRESSION: str = 'zip'
# Rotation log file.
LOGGER_ROTATION: str = '10 MB'

# PostgreSQL database URL.
DATABASE_URL: str = os.getenv('DATABASE_URL')
# Maximum connections to PostgreSQL database.
MAX_DB_CONNECTIONS: int = os.getenv('MAX_DB_CONNECTIONS', 10)
# Minimum connections to PostgreSQL database.
MIN_DB_CONNECTIONS: int = os.getenv('MIN_DB_CONNECTIONS', 10)

# The path to the bot commands that will work.
EXTENSION_PATH_LIST: list[str] = [
    'ukrfans.events.error',
    'ukrfans.events.message',
    'ukrfans.modules.moderation',
    'ukrfans.modules.information',
    'ukrfans.modules.utility',
    'ukrfans.modules.social_rating'
]

# Testing guilds id list.
TEST_GUILDS: list[int] = [
    851185360146923520
]

# Like channels id list.
LIKE_CHANNELS: list[int] = [
    989627210296090624,
    989627366173179924,
    989627416915890236
]
