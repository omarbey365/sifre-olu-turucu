import discord
from discord.ext import commands
from a import mert
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
@bot.command()
async def apo(ctx):
    await ctx.send(f'ben apo')
    
@bot.command()
async def aaaa(ctx):
    await ctx.send(mert(10))
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

#Buraya token gelecek
