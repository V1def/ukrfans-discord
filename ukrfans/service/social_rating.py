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

"""User social rating service."""

import asyncpg

from ..repository.social_rating import Repository


class Service:
    """User social rating service."""

    def __init__(self, db_pool: asyncpg.Pool) -> None:
        self.repos = Repository(db_pool)

    async def vote(self, user_id: int, voted_id: int, status: bool) -> int:
        """Vote for the user social rating."""
        return await self.repos.vote(user_id, voted_id, status)

    async def get(self, user_id: int) -> int:
        """Get user social rating."""
        return await self.repos.get(user_id)

    async def delete(self, user_id: int, voted_id: int) -> None:
        """Delete user vote."""
        return await self.repos.delete(user_id, voted_id)
