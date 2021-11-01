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

from typing import Optional

import disnake
from disnake.ext import commands

from .. import config, param
from ..core.bot import Bot


class Information(commands.Cog):
    """Information commands."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="github",
        description="Команда надсилає посилання на репозиторій бота."
    )
    async def github(self, inter: disnake.MessageCommandInteraction) -> None:
        """The command sends the bot github repository."""
        # Create and send embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            title="Вихідний код бота <:ukrfans:895677507276263476>",
            description="https://github.com/V1def/ukrfans-discord"
        )

        await inter.response.send_message(embed=embed)

    @commands.guild_only()
    @commands.slash_command(
        name="сервер",
        description="Команда виводить всю доступну інформацію про даний сервер."
    )
    async def server(self, inter: disnake.MessageCommandInteraction) -> None:
        """The command sends all available information about this guild."""
        # Creating a new embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            title=f"Інформація про {inter.guild.name}"
        )
        # Add to embed time stamp guild creating date.
        embed.timestamp = inter.guild.created_at
        # Add to embed thumbnail guild avatar.
        embed.set_thumbnail(url=inter.guild.icon.url)
        # Embed members field.
        embed.add_field(
            name="Учасники:",
            inline=False,
            value=(
                f"> :busts_in_silhouette: Кількість: **{inter.guild.member_count}**"
            )
        )
        # Embed channels filed.
        embed.add_field(
            name="Канали:",
            inline=False,
            value=(
                f"> :pushpin: Категорій: **{len(inter.guild.categories)}**\n"
                f"> :pencil: Текстових: **{len(inter.guild.text_channels)}**\n"
                f"> :loud_sound: Голосових: **{len(inter.guild.voice_channels)}**"
            )
        )
        # Embed guild field.
        embed.add_field(
            name="Сервер:",
            inline=False,
            value=(
                f"> :scales: Ролів: **{len(inter.guild.roles)}**\n"
                f"> :ice_cube: Емодзі: **{len(inter.guild.emojis)}**\n"
                f"> :blue_book: Вебхуків: **{len(await inter.guild.webhooks())}**\n"
                f"> :lock: Блокувань: **{len(await inter.guild.bans())}**\n"
                f"> :diamonds: Бустерів: **{len(inter.guild.premium_subscribers)}"
                f" ({inter.guild.premium_subscription_count})**\n"
                f"> :crown: Власник: **{inter.guild.owner}**"
            )
        )
        # Set embed footer.
        embed.set_footer(text="Сервер створений", icon_url=inter.author.avatar.url)

        await inter.response.send_message(embed=embed)

    @commands.slash_command(
        name="користувач",
        description="Команда виводить всю доступну інформацію про користувача."
    )
    async def user(
        self,
        inter: disnake.MessageCommandInteraction,
        member: Optional[disnake.Member] = param.optional_member_param
    ) -> None:
        """The command sends all available information about user."""
        if member is None:
            member = inter.author

        # Creating a new embed.
        embed = disnake.Embed(
            color=config.EMBED_COLOR,
            title=f"Інформація про {member}"
        )
        # Add to embed thumbnail member avatar.
        embed.set_thumbnail(url=member.avatar.url)
        # Member time information field.
        embed.add_field(
            name="Часова інформація:",
            inline=False,
            value=(
                f"> :calendar: Cтворено: **{member.created_at.strftime('%m.%d.%Y %H:%M')}**\n"
                f"> :stopwatch: Приєднався: **{member.joined_at.strftime('%m.%d.%Y %H:%M')}**\n"
            )
        )
        # Set embed footer.
        embed.set_footer(text=f"ID: {member.id}", icon_url=member.avatar.url)
        await inter.response.send_message(embed=embed)


def setup(bot: Bot) -> None:
    """Adding cog to bot."""
    bot.add_cog(Information(bot))
