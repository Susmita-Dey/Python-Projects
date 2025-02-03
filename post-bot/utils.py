import traceback
import discord
import discord.utils
from discord.ext import commands


def make_default_embed(title: str, message: str, author: str) -> discord.Embed:
    """
    Produces an embed with the default presentation.

    Arguments:
        title (str): Title for the embed.
        message (str): Message for the main body of the embed.
        author (str): Display name of the author of the embed.

    Returns:
        discord.Embed: An embed with the default template and the given content.
    """
    embed = discord.Embed(
        title=title,
        description=message,
        color=0xFFD700,  # Gold color for the embed border
    )
    # Add a footer to the embed
    embed.set_footer(text=f"- {author}")
    return embed


def author_has_permission(ctx, allowed_role_id):
    role = discord.utils.get(ctx.guild.roles, id=allowed_role_id)
    return role in ctx.author.roles


async def post_to_channel(
    ctx: commands.Context, message: str, channel_id: int, title: str
):
    """
    Posts given message with given title to channel with given id.

    Arguments:
        ctx (discord.ext.commands.Context): Context under which the command was invoked.
        message (str): Message to be sent.
        channel_id (int): ID of the channel to which the message will be sent.
        title (str): Title of the embed to put in the message.
    """
    try:
        # Get channel and confirm that it exists
        channel = ctx.guild.get_channel(channel_id)
        if not channel:
            await ctx.send("Target channel not found.")
            return
        # Send embed and delete original command message
        embed = make_default_embed(title, message, ctx.author.display_name)
        await channel.send(embed=embed)
        await ctx.message.delete()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        await ctx.send("An error occurred while trying to execute the command.")
