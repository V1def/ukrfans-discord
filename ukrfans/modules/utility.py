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

"""Utility bot commands."""

import disnake
from disnake.ext import commands

from .. import config, param
from ..core.bot import Bot


class Utility(commands.Cog):
    """Utility commands."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="аватар",
        description="Команда виводить аватар учасника."
    )
    async def avatar(
        self,
        inter: disnake.MessageCommandInteraction,
        member: disnake.Member = param.optional_member_param
    ) -> None:
        """The command sends the member avatar."""
        # Member identity ckeck.
        if member is None:
            member = inter.author

        # Create and add member avatar to embed and send.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            title=f"Аватар {member}"
        )
        embed.set_image(member.avatar.url)

        await inter.response.send_message(embed=embed)


def setup(bot: Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Utility(bot))
