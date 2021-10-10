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

"""Configure handlers and formats for bot loggers."""

import logging
import sys

from loguru import logger

from .. import config


class InterceptHandler(logging.Handler):
    """Default handler from examples in loguru documentation."""

    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logger message.
        frame, depth = logging.currentframe(), 2

        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def init_logging() -> None:
    """Replaces logging handlers with a handler for using the custom handler."""
    # Change handler for default aioredis logger
    intercept_handler = InterceptHandler()
    logging.getLogger('disnake').handlers = [intercept_handler]

    # Set logs output, level and format
    LOGGING_LEVEL = logging.DEBUG if config.DEBUG else logging.INFO

    logger.configure(
        handlers=[
            {
                'sink': sys.stdout,
                'level': LOGGING_LEVEL,
                'format': (
                    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                    "<level>{level: <7}</level> | <level>{message}</level>"
                ),
            },
        ]
    )

    # Record logs to a file
    logger.add(
        config.LOG_FILE_PATH, compression=config.LOGGER_COMPRESSION,
        level=LOGGING_LEVEL, rotation=config.LOGGER_ROTATION,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <7} | {message}",
    )
