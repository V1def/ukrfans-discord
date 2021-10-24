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

from typing import Optional

import disnake
from disnake.ext import commands

from .. import config, errors, param


async def send_mod_embed(
    inter: disnake.MessageCommandInteraction,
    description: str,
    reason: Optional[str] = None
) -> None:
    """Send moderaton embed to the guild."""
    # Creating a new discord embed.
    embed = disnake.Embed(
        color=config.EMBED_COLOR,
        description=description
    )

    # Check fot indication of the reason.
    if reason is not None:
        embed.add_field(
            name=":envelope: По причині:",
            value=f"*{reason}*",
            inline=False
        )

    await inter.response.send_message(embed=embed)


async def send_private_mod_embed(
    member: disnake.Member,
    description: str,
    reason: Optional[str] = None
) -> None:
    """Send private moderaton embed to the guild."""
    # Creating a new discord embed.
    embed = disnake.Embed(
        color=config.EMBED_COLOR,
        description=description
    )

    # Check fot indication of the reason.
    if reason is not None:
        embed.add_field(
            name=":envelope: По причині:",
            value=f"*{reason}*",
            inline=False
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
        reason: Optional[str] = param.reason_param
    ) -> None:
        """The command that expels the specified member from the guild"""
        # Check to execute the command.
        if member.id in (inter.author.id, inter.guild.owner.id):
            raise errors.MemberProtected
        elif inter.author.top_role.position < member.top_role.position:
            if inter.author.id != inter.guild.owner.id:
                raise errors.MemberTopRolePosition

        # Send embed to channel.
        await send_mod_embed(
            inter, f"Учасник {member} був вигнаний з сервера :neutral_face:", reason
        )

        # Send embed to member dm.
        await send_private_mod_embed(
            member, f"Ти був вигнаний з сервера {inter.guild} :confused:", reason
        )

        # Kick member in the guild.
        await member.kick(reason=reason)

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(
        name="заблокувати",
        description="Команда блокує вказаного вами учасника на сервері."
    )
    async def ban(
        self,
        inter: disnake.MessageCommandInteraction,
        member: disnake.Member = param.member_param,
        reason: Optional[str] = param.reason_param,
        delete_message_days: int = param.delete_message_days_param
    ) -> None:
        """The command that blocked the specified member from the guild"""
        # Check to execute the command.
        if member.id in (inter.author.id, inter.guild.owner.id):
            raise errors.MemberProtected
        elif inter.author.top_role.position < member.top_role.position:
            if inter.author.id != inter.guild.owner.id:
                raise errors.MemberTopRolePosition

        # Send embed to channel.
        await send_mod_embed(
            inter, f"Учасник {member} був заблокований на сервері :frowning2:", reason
        )

        # Send embed to member dm.
        await send_private_mod_embed(
            member, f"Ти був заблокований на сервері {inter.guild} :no_mouth:", reason
        )

        # Ban member in the guild.
        await member.ban(
            reason=reason,
            delete_message_days=delete_message_days
        )

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(
        name="розблокувати",
        description="Команда розблоковує вказаного вами учасника на сервері."
    )
    async def unban(
        self,
        inter: disnake.MessageCommandInteraction,
        user: str = param.user_param,
        reason: Optional[str] = param.reason_param
    ) -> None:
        """The command that unblock the specified user from the guild."""
        bans = await inter.guild.bans()
        name, discriminator = user.split('#')

        # Search for a user in guild bans.
        for users in bans:
            ban_user = users.user

            # User verification.
            if (ban_user.name, ban_user.discriminator) == (name, discriminator):
                await send_mod_embed(
                    inter, f"Користувач **{user}** був розблокований! :partying_face:", reason
                )
                # Unban user in the guild.
                await inter.guild.unban(user, reason)

        # Send a message if the user was not found.
        await send_mod_embed(inter, f"Користувача **{user}** не було знайдено! :man_shrugging:")


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Moderation(bot))
