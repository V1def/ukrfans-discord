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

"""Discord slash commands parameters."""

from typing import Dict

from disnake.ext.commands import Param

# Discord guild member parameter.
member_param = Param(
    name="учасник",
    desc="Вкажіть учасника."
)

# Discord optional guild member parameter.
optional_member_param = Param(
    None,
    name="учасник",
    desc="Вкажіть учасника."
)

# Reason parameter.
reason_param = Param(
    None,
    name="причина",
    desc="Вкажіть причину."
)

# Delete message in days choices.
delete_message_days_choices: Dict[str, int] = {
    "Не видаляти": 0,
    "За 1 день": 1,
    "За 2 дні": 2,
    "За 3 дня": 3,
    "За 4 днів": 4,
    "За 5 днів": 5,
    "За 6 днів": 6,
    "За 7 днів": 7
}

# Delete message in days parameter.
delete_message_days_param = Param(
    0,
    name="видалити-повідомлення",
    desc="Виберіть кількість днів.",
    choices=delete_message_days_choices
)

# Discord user name parameter.
user_param = Param(
    name="користувач",
    desc="Вкажіть користувача з його тегом, приклад: User#0000"
)
