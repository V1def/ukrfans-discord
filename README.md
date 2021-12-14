<h1 align="center">Ukrfans Discord Bot</h1>

<p align="center">
Discord bot for Ukrfans Discord server.
</p>

### 💡 Prerequisites
+ [Python](https://www.python.org/)
+ [migrate](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate)

## ⚙️ Build & Run
1) The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/V1def/ukrfans-discord.git
$ cd ukrfans-discord
```
2) Create a virtual environment to install dependencies in and active it:

**Windows:**
```sh
$ python -m venv venv
$ .\env\Scripts\activate
```

**macOS and Linux:**
```sh
$ python3 venv venv
$ source env/bin/activate
```
3) Then install the dependencies:
```sh
(venv) make install
```
4) Create an `.env` file in the root directory and add the following values ​​from `.env.example`:
```env
# Discord bot token.
BOT_TOKEN=
# Reconnecting bot.
BOT_RECONNECT=true
# Debug mode.
DEBUG=false

# PostgreSQL database URL.
DATABASE_URL=
```
Use `make run` to run bot.

## ⚠️ License
Copyright © 2021 [V1def](https://github.com/V1def). Released under the [GNU AGPL v3](https://www.gnu.org/licenses/agpl-3.0.html) license.

#### Third-party library licenses
+ [disnake](https://github.com/DisnakeDev/disnake/blob/master/LICENSE)
+ [python-dotenv](https://github.com/theskumar/python-dotenv/blob/master/LICENSE)
+ [loguru](https://github.com/Delgan/loguru/blob/master/LICENSE)
+ [asyncpg](https://github.com/MagicStack/asyncpg/blob/master/LICENSE)
