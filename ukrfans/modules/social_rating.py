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

"""Social rating bot commands."""

from typing import Optional

import disnake
from disnake.ext import commands

from .. import param, errors, config
from ..core.bot import Bot
from ..service.social_rating import Service


class SocialRating(commands.Cog):
    """Social rating commands."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.service = Service(bot.db_pool)

    @commands.slash_command(
        name="рейтинг",
        description="Команда виводить соціальний рейтинг користувача."
    )
    async def rating(
        self,
        inter: disnake.MessageCommandInteraction,
        member: Optional[disnake.Member] = param.optional_member_param,
    ) -> None:
        """Display the user social rating."""
        if member is None:
            member = inter.author

        # Get user social rating.
        rating = await self.service.get(member.id)

        # Create a new embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            description=f"Соціальний рейтинг {member.mention}: **{rating}**"
        )

        await inter.response.send_message(embed=embed)

    @commands.slash_command(
        name="голос",
        description="Команда змінює соціальний рейтинг вказаного вами користувача."
    )
    async def change_vote(
        self,
        inter: disnake.MessageCommandInteraction,
        member: Optional[disnake.Member] = param.member_param,
        rating: int = param.social_rating_param
    ) -> None:
        """Changes the social rating of the user you specified."""
        if member.id == inter.author.id:
            raise errors.MemberProtected
        elif rating == 2:
            await self.service.delete(member.id, inter.author.id)

            # Create a new embed.
            embed = disnake.Embed(
                color=config.EMBED_COLOR,
                description=f"Ви видалили свій голос з соціального рейтингу {member.mention}"
            )

            return await inter.response.send_message(embed=embed, ephemeral=True)

        # Adding or changing the vote.
        vote_id = await self.service.vote(member.id, inter.author.id, bool(rating))
        if vote_id == 0:
            raise errors.AlreadyUsed

        # Social rating table.
        rating_table: dict[int, str] = {
            0: "зменшили",
            1: "збільшили"
        }

        # Create a new embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            description=f"Ви {rating_table[rating]} соціальний рейтинг користувача {member.mention}"
        )

        await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot: Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(SocialRating(bot))
