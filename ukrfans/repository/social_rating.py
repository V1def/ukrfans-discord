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

"""User social rating repository."""

import asyncpg


social_rating_table = "social_rating"


class Repository:
    """User social rating repository."""

    def __init__(self, db_pool: asyncpg.Pool) -> None:
        self.db_pool = db_pool

    async def add(self, user_id: int, voted_id: int, status: bool) -> int:
        """Create a new user vote."""
        query = f"""
        INSERT INTO {social_rating_table}
        (user_id, voted_id, status)
        VALUES ($1, $2, $3)
        RETURNING id
        """

        return await self.db_pool.execute(query, user_id, voted_id, status)

    async def vote(self, user_id: int, voted_id: int, status: bool) -> int:
        """Vote for the user social rating."""

        # Check user vote.
        query = f"SELECT status FROM {social_rating_table} WHERE user_id = $1 AND voted_id = $2"
        vote = await self.db_pool.fetchrow(query, user_id, voted_id)

        if vote is None:
            return await self.add(user_id, voted_id, status)
        elif status == vote[0]:
            return 0

        # Create a new user vote.
        query = f"""
        UPDATE {social_rating_table} SET status=$1
        WHERE user_id = $2 AND voted_id = $3 RETURNING id
        """

        return await self.db_pool.execute(query, status, user_id, voted_id)

    async def get(self, user_id: int) -> int:
        """Get user social rating."""
        # Get all user count votes.
        query = f"SELECT COUNT (*) FROM {social_rating_table} WHERE user_id = $1 AND status = true"
        good_count = await self.db_pool.fetchrow(query, user_id)

        # Get all user bad count votes.
        query = f"SELECT COUNT (*) FROM {social_rating_table} WHERE user_id = $1 AND status = false"
        bad_count = await self.db_pool.fetchrow(query, user_id)

        return good_count[0] - bad_count[0]

    async def delete(self, user_id: int, voted_id: int) -> None:
        """Delete user vote."""
        query = f"DELETE FROM {social_rating_table} WHERE user_id = $1 AND voted_id = $2"

        await self.db_pool.execute(query, user_id, voted_id)
