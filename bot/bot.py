import json
import sys
from discord import HTTPException
from discord.ext.commands import Bot

# Note: Copy the default_config.json file, and rename the copy to config.json
#       add your token to that file and avoid sharing it to avoid leaking your token.

# load the json file which contains our configs.
with open("config.json") as file:
    config = json.load(file)

# gets the prefix, and token from the config. Prefix has a default fallback to "!"
prefix = config.get("prefix", "!")
token = config.get("token")

# Defines the bot instance
bot = Bot(command_prefix=prefix)


def load_extensions():
    """
    Loads all extensions for the bot
    extensions is the name of a .py file which contains a cog
    without the .py suffix.  The method call also requires a relative
    path represented with . notation.
    """

    bot.load_extension("cogs.hello_world")
    bot.load_extension("cogs.example")
    # additional cogs would be loaded here


def start():
    """
    Loads the extensions (cogs) for the bot
    then attempts to start the bot with run.

    If the token is invalid run will raise a HTTPException
    and the program will terminate
    """

    load_extensions()

    try:
        bot.run(token)

    except HTTPException:
        print("Token is invalid")
        sys.exit(1)


if __name__ == "__main__":
    if token:
        start()
    else:
        # if the config does not contain a token the script will shutdown
        print("No token set in config.json!")
        sys.exit(1)


