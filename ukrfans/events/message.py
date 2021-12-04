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

"""All messages seen by the bot are processed."""

import disnake
from disnake.ext import commands

from .. import config


class Message(commands.Cog):
    """Message handler."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message) -> None:
        """The event is triggered by a new message."""
        if message.channel.id in config.LIKE_CHANNELS:
            await message.add_reaction('👍')
            await message.add_reaction('👎')


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Message(bot))
