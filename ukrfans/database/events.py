# Copyright © 2021 V1def

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

"""Events connecting and disconnecting to the PostgreSQL database."""

import asyncpg
from disnake.ext.commands import Bot
from loguru import logger

from .. import config


async def connect_to_db(bot: Bot) -> None:
    """PostgreSQL database connection."""
    logger.info("Connecting to PostgreSQL database...")

    try:
        bot.db_pool = await asyncpg.create_pool(
            str(config.DATABASE_URL),
            max_size=config.MAX_DB_CONNECTIONS,
            min_size=config.MIN_DB_CONNECTIONS
        )
        logger.info("Connection to DataBase established!")
    except Exception as e:
        logger.error("Error connection to PostgreSQL database: {error}", error=e)


async def close_db_connection(bot: Bot) -> None:
    """Close the PostgreSQL database. connection."""
    logger.info("Closing connection to PostgreSQL database...")

    try:
        await bot.db_pool.close()

        logger.info("Connection to PostgreSQL database closed!")
    except Exception as e:
        logger.error("Error close to PostgreSQL database connection: {error}", error=e)
