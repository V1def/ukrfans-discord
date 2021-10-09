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

from .. import errors


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
        if isinstance(error, errors.MemberProtected):
            return await inter.response.send_message("test message")


def setup(bot: commands.Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Error(bot))
