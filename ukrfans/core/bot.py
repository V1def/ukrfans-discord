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

"""The main file of the bot that is responsible for its connection and operation."""

from disnake.ext import commands
from loguru import logger

from .. import config


class Bot(commands.InteractionBot):
    """The main class the bot."""

    def __init__(self) -> None:
        super().__init__(
            intents=config.BOT_INTENTS,
            test_guilds=config.TEST_GUILDS
        )

    def load_extension(self) -> None:
        """Load bot extension."""
        logger.info("Loading bot extensions...")

        for extension in config.EXTENSION_PATH_LIST:
            try:
                super().load_extension(extension)
            except Exception as e:
                logger.error(
                    "Failed to load extension {extension}: {error}",
                    extension=extension, error=e
                )
            else:
                logger.info("Extension '{extension}' loaded!", extension=extension)

    def run(self) -> None:
        """Running the bot."""
        # Running the bot with a token.
        self.load_extension()
        super().run(config.BOT_TOKEN, reconnect=config.BOT_RECONNECT)

    async def on_connect(self) -> None:
        """Called when the bot is connected."""
        logger.info("Bot connected!")

    async def on_disconnect(self) -> None:
        """Called when the bot is disabled."""
        logger.warning("No internet access!")

    async def on_ready(self) -> None:
        """Called when the bot is ready."""
        logger.info("Bot ready!")
