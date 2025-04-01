import discord
import os
from discord.ext import commands
# Setup the bot
TOKEN = "MTM1NjYxNjM0Njc0NTQzODQzOQ.GLDVLY.VXGcBQoYGPMFIpCxuObMTnfwDT4KCiHzkZ35l8"  # Get token from environment variable
intents = discord.Intents.default()
intents.messages = True  # This ensures the bot can read messages
intents.message_content = True  # This is the key fix!

bot = commands.Bot(command_prefix="!", intents=intents)

# Pre-coded links dictionary
links = {
    "bts":
    "https://cdn.discordapp.com/attachments/446620239837265920/1356609214201467125/20250401_180616.jpg?ex=67ed3049&is=67ebdec9&hm=b9f3363d4fbee4f37881114541f6e1e733a6e5f1ad1276691dc940f34cbcdeb6&",
    "gn":
    "https://cdn.discordapp.com/attachments/468063675421294593/1330217988409786511/20250105_064952.jpg?ex=67ecc24a&is=67eb70ca&hm=7de414e045b6fbbefa0b96083121dc451d99632bd05399f5fccc6c546cf2cf64&"
}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def link(ctx, name: str):
    """Replies with a pre-coded link based on command input."""
    if name in links:
        await ctx.send(links[name])
    else:
        await ctx.send("Link not found! Try: " + ", ".join(links.keys()))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Received message: {message.content}")
    await bot.process_commands(message)


# Run the bot
if TOKEN is None:
    print("DISCORD_BOT_TOKEN environment variable not set. Exiting.")
    exit(1)
bot.run(TOKEN)
keep_alive()  # Start the web server
bot.run(TOKEN)
