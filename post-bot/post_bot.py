from functools import partial, wraps
import discord
from discord.ext import commands
from utils import post_to_channel, author_has_permission


class PostBot:
    def __init__(self, allowed_role_id, job_channel_id, service_channel_id):
        intents = discord.Intents.default()
        intents.message_content = True
        self.allowed_role_id = allowed_role_id
        self.job_channel_id = job_channel_id
        self.service_channel_id = service_channel_id
        self.bot = commands.Bot(command_prefix="/", intents=intents)

        # Add commands and listeners
        self.bot.event(self.on_ready)
        self.add_command("postjob", PostBot.post_job)
        self.add_command("postservices", PostBot.post_services)
        self.add_command("post", PostBot.post)

    def add_command(self, name, f):
        self.bot.command(name=name)(wraps(f)(partial(f, self)))

    def run(self, token):
        self.bot.run(token)

    async def on_ready(self):
        print(f"Bot is ready. Logged in as {self.bot.user}")

    async def post_job(self, ctx, *, message: str):
        # Check if the author has the allowed role ID
        if not author_has_permission(ctx, self.allowed_role_id):
            await ctx.send("You do not have the required role to use this command.")
            return
        await post_to_channel(ctx, message, self.job_channel_id, "New Job Posting")

    async def post_services(self, ctx, *, message: str):
        if not author_has_permission(ctx, self.allowed_role_id):
            await ctx.send("You do not have the required role to use this command.")
            return
        await post_to_channel(
            ctx, message, self.service_channel_id, "New Service Offering"
        )

    async def post(
        self, ctx, channel: discord.TextChannel, title: str, *, message: str
    ):
        if not author_has_permission(ctx, self.allowed_role_id):
            await ctx.send("You do not have the required role to use this command.")
            return
        await post_to_channel(ctx, message, channel.id, title)
