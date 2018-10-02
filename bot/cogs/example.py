import random
from discord.ext import commands


class Example:
    """
    Cleaner example of a cog without all the docstring
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx, max_num: int=6):
        """
        Rolls the dice!
        :param max_num: defaults to 6, can set the max roll number
        """

        roll = random.randint(1, max_num)
        await ctx.send(f"The dice says... {roll}")


def setup(bot):
    bot.add_cog(Example(bot))
