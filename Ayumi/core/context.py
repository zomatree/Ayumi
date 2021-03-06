"""
Ayumi - Discord bot
Copyright (C) 2020 - Saphielle Akiyama | saphielle.akiyama@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import functools
import typing as tp
import aioredis
from discord.ext import commands


class Context(commands.Context):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._altered_cache_key = None

    @functools.cached_property
    def cname(self) -> tp.Union[str, None]:
        """Shortcut for ctx.command.name"""
        return getattr(self.command, 'name', None)

    @functools.cached_property
    def qname(self) -> tp.Union[str, None]:
        """Shortcut for ctx.command.qualified_name"""
        return getattr(self.command, 'qualified_name', None)

    @functools.cached_property
    def all_args(self) -> list:
        """Returns a list of args and kwargs passed to the command, might be incomplete too"""
        args = self.args[2:] if self.command.cog else self.args[1:]

        kwargs = [*self.kwargs.values()]

        return args + kwargs

    @property
    def cache_key(self) -> str:
        """Returns a string that is used as the cache key"""

        list_key = self._altered_cache_key or ([self.qname] + [*map(str, self.all_args)])

        return ' '.join(list_key)

    @cache_key.setter
    def cache_key(self, key: str) -> None:
        """Sets another key to use for this context"""

        if not isinstance(key, (list, tuple)):
            raise TypeError("Cache key must be a list or a tuple")

        self._altered_cache_key = key

    @property
    def redis(self) -> aioredis.Redis:
        """Returns the bot's redis"""
        return self.bot.redis
