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

"""Moderation bot commands."""

import disnake
from disnake.ext import commands

from .. import config, param


async def send_mod_embed(
    inter: disnake.MessageCommandInteraction,
    description: str,
    reason: str = None
) -> None:
    """Send moderaton embed to the guild."""
    # Creating a new discord embed.
    embed = disnake.Embed(
        color=config.EMBED_COLOR,
        description=description
    )

    # Check fot indication of the reason.
    if not (reason is None):
        embed.add_field(
            name=":envelope: По причині:", value=f"*{reason}*", inline=False
        )

    await inter.response.send_message(embed=embed)


async def send_private_mod_embed(
    member: disnake.Member,
    description: str,
    reason: str = None
) -> None:
    """Send private moderaton embed to the guild."""
    # Creating a new discord embed.
    embed = disnake.Embed(
        color=config.EMBED_COLOR,
        description=description
    )

    # Check fot indication of the reason.
    if not (reason is None):
        embed.add_field(
            name=":envelope: По причині:", value=f"*{reason}*", inline=False
        )

    await member.send(embed=embed)


class Moderation(commands.Cog):
    """Moderation commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.slash_command(
        name="вигнати",
        description="Команда виганяє вказаного вами учасника з серверу."
    )
    async def kick(
        self,
        inter: disnake.MessageCommandInteraction,
        member: disnake.Member = param.member_param,
        reason: str = param.reason_param
    ) -> None:
        """The command that expels the specified member from the guild"""
        # Check to execute the command.
        if inter.author.id == member.id and inter.guild.owner.id:
            raise NotImplementedError  # Soon to be
        elif inter.author.top_role.position < member.top_role.position:
            if inter.author.id != inter.guild.owner.id:
                raise NotImplementedError  # Soon to be

        await send_mod_embed(
            inter, f"Учасник {member} був вигнаний з сервера :neutral_face:",
            reason
        )

        await send_private_mod_embed(
            member, f"Ти був вигнаний з сервера {inter.guild} :confused:",
            reason
        )

        await member.kick(reason)


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Moderation(bot))
