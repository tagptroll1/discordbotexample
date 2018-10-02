from discord import Message
from discord.ext import commands
from discord.ext.commands import Bot


class HelloWorld:
    """
    A cog for our bot named HelloWorld.
    Behaves like a normal class, but discord.py reads it's content
    in order to load cogs, queue event listeners e.g

    This is a simple cog to demonstrate many of the core
    features of using the discord.py library
    """

    def __init__(self, bot: Bot):
        """
        Instantiates the cog, and stores a reference to the bot

        :param bot: reference to the bot created in bot.py
        """

        self.bot = bot

    async def on_message(self, message: Message):
        """
        One of the more used events.
        Whenever a message is sent, and the bot can read it, the
        message is passed to this event as a Message object (message param)

        :param message: The message caught as a discord.Message instance
        """

        # We simply echo the messages the bot reads to our console
        print(f"{str(message.author)}: {message.content}")

    @commands.command(name="helloworld", aliases="hello")
    async def hello_world(self, ctx):
        """
        Simple hello world command.
        A command is called using the prefix set in bot.py + it's method name.
        (Unless the name parameter is set in the decorator)
        i.e "!hello_world

        This command has the name parameter set, so the method name is not used
        for this command. The decorator also sets an alias for the command as "hello" which
        allows it to be called by writing "!helloworld" and "!hello"

        :param ctx: An object which contains all of the data related to the command call
                    Data like the author, content, channel etc.
        """

        author = ctx.author.display_name
        await ctx.send(f"Hello World, and hello to you {author}!")

    @commands.command(aliases=["pingme", "dmme"])
    async def whisperme(self, ctx, *, content="Hello"):
        """
        Echoes a message back to the author, or "Hello" if no
        message is provided with the command.

        Usage examples:
        "!whisperme", "!dmme", "!pingme Hello me Hi!"

        :param ctx: The context object for this command call
        :param content: Content to be echoed back, defaults to "Hello"
        """

        author = ctx.author
        await author.send(content)


def setup(bot):
    """
    This function is required for `bot.load_extension` to work when loading the cog.
    load_extension passes the bot to a setup function, and the cog is added to
    the bot through this function.

    :param bot: The bot instance created in bot.py
    """

    bot.add_cog(HelloWorld(bot))
