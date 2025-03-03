import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1345727973550067802

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """
    Ensures the bot is fully ready before sending the embed.
    """
    await asyncio.sleep(2)  # need this delay or else it tries to run before it gets ready and doesn't work
    print(f"✅ Logged in as {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="",
            description="Play a chill playlist for coding!",
            color=0x1DB954
        )
        
        image_url = "https://i.ibb.co/G4gPpkp8/yt-music-pic-1-1.png"
        embed.set_author(name="Youtube Music", icon_url=image_url)
        await channel.send(embed=embed)
        print(f"📨 Sent message in #{channel.name}!")
    else:
        print("❌ ERROR: Could not find the channel.")

bot.run(TOKEN)