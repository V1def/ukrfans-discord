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

"""Here are the errors that can be caused by the bot."""

from typing import Optional

from disnake.ext.commands.errors import CommandError


class MemberTopRolePosition(CommandError):
    """If the specified member is higher for you in the role."""
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message or "the specified member above you in the role."
        )


class MemberProtected(CommandError):
    """If the specified member is the author or owner."""
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message or "the specified member is the author or owner."
        )
