import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        raise ValueError("Le token Discord est introuvable. Vérifie le fichier .env ou les variables d'environnement.")
    bot.run(token)
