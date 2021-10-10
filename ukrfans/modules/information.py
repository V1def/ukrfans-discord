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

"""Information bot commands."""

import disnake
from disnake.ext import commands

from .. import config


class Information(commands.Cog):
    """Information commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="github",
        description="Команда надсилає посилання на репозиторій бота."
    )
    async def kick(self, inter: disnake.MessageCommandInteraction,) -> None:
        """The command sends the bot github repository."""
        # Create and send embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            title="Вихідний код бота <:ukrfans:895677507276263476>",
            description="https://github.com/V1def/ukrfans-discord"
        )

        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Information(bot))
