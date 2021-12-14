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

"""Processing of all bot errors."""

import disnake
from disnake.ext import commands

from .. import errors, config


async def send_debug_slash_error(
    inter: disnake.MessageCommandInteraction,
    error: commands.CommandError
) -> None:
    """Send slash debug error."""
    # Creating a new discird embed.
    embed = disnake.Embed(
        color=config.EMBED_ERROR_COLOR,
        title="Сталася помилка :thinking:",
        description=error
    )
    embed.set_footer(
        text="Увімкнений DEBUG режим",
        icon_url=inter.author.avatar.url
    )

    await inter.response.send_message(embed=embed, ephemeral=True)


async def send_slash_error(
    inter: disnake.MessageCommandInteraction,
    description: str
) -> None:
    """Send slash error."""
    # Creating a new discird embed.
    embed = disnake.Embed(
        color=config.EMBED_COLOR,
        description=f"{inter.author.mention}, {description}"
    )

    await inter.response.send_message(embed=embed, ephemeral=True)


class Error(commands.Cog):
    """Error handlers."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(
        self,
        inter: disnake.MessageCommandInteraction,
        error: commands.CommandError
    ) -> None:
        """Slash commands error handling."""
        # If command not found.
        if isinstance(error, commands.CommandNotFound):
            return
        # Send debug error.
        elif config.DEBUG:
            return await send_debug_slash_error(inter, error)
        # If the specified member is the author or owner.
        elif isinstance(error, errors.MemberProtected):
            return await send_slash_error(
                inter, "цю команду не можна використати на собі або власникові! :slight_smile:"
            )
        # If the specified member is higher for you in the role.
        elif isinstance(error, errors.MemberTopRolePosition):
            return await send_slash_error(
                inter, "цю команду не можна використати на учаснику вище тебе по ролі! :wink:"
            )
        # If the command is already used.
        elif isinstance(error, errors.AlreadyUsed):
            return await send_slash_error(
                inter, "ти вже використав цю команду! :shushing_face:"
            )


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Error(bot))
