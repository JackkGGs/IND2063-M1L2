from config import token
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)
        
@client.command()
async def about(ctx):
       await ctx.send("Ini adalah echo bot yang dibuat dengan library discord.py!")
@client.command()
async def info(ctx):
       await ctx.send("Infokan le 😈😈")

@client.command()       
async def wallpaper(ctx, filename="wallpaper.jpg"):
    folder_path = os.path.join(os.getcwd(), 'images')

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await ctx.send("The 'images' folder does not exist in the same directory.")
        return

    file_path = os.path.join(folder_path, filename)

    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif']
    if not any(file_path.lower().endswith(ext) for ext in allowed_extensions):
        await ctx.send("Invalid file type. Only .png, .jpg, .jpeg, and .gif files are allowed.")
        return

    if os.path.exists(file_path) and os.path.isfile(file_path):
        file_to_attach = discord.File(file_path)
        await ctx.send(files=[file_to_attach])
    else:
        await ctx.send(f"File '{filename}' not found in the 'images' folder.")
        
@client.command()
async def chillsong(ctx, filename="U Weren’t Here I Really Miss You (Original Mix).mp3"):
    folder_path = os.path.join(os.getcwd(), 'audios')

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await ctx.send("The 'audios' folder does not exist in the same directory.")
        return

    file_path = os.path.join(folder_path, filename)

    allowed_extensions = ['.mp3', '.wav', '.ogg', '.flac']
    if not any(file_path.lower().endswith(ext) for ext in allowed_extensions):
        await ctx.send("Invalid file type. Only .mp3, .wav, .ogg, and .flac files are allowed.")
        return

    if os.path.exists(file_path) and os.path.isfile(file_path):
        file_to_attach = discord.File(file_path)
        await ctx.send(files=[file_to_attach])
    else:
        await ctx.send(f"File '{filename}' not found in the 'audios' folder.")

client.run(token=token)

client.run(token=token)
