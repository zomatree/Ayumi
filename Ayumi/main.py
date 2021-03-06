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

import os

import discord

import core


if __name__ == '__main__':

    # Jishaku env

    for env in ('NO_UNDERSCORE', 'HIDE', 'RETAIN'):
        os.environ['JISHAKU_' + env] = 'True'

    # Bot
    bot = core.Bot(max_messages=None,
                   fetch_offline_members=False,
                   guild_subscriptions=False,
                   allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False))

    bot.run()
