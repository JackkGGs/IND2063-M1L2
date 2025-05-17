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
       await ctx.send("""Ini adalah echo bot yang dibuat dengan library discord.py!
       Kirim /info untuk mengetahui lebih.""")
    
@client.command()
async def info(ctx):
       await ctx.send("""Ini adalah bot untuk me-return suatu gambar.
       Bot ini hanya sekedar bot untuk testing.
       
       Gunakan /imagetest untuk menjalankan fungsi tersebut.""")
       
@client.command()
async def imagetest(ctx):
    folder_path = os.path.join(os.getcwd(), 'images')

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await ctx.send("The 'images' folder does not exist in the same directory.")
        return

    files_to_attach = []
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif'] # Add more if needed

    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in allowed_extensions):
            file_path = os.path.join(folder_path, filename)
            files_to_attach.append(discord.File(file_path))

    if files_to_attach:
        await ctx.send(files=files_to_attach)
    else:
        await ctx.send("No image files found in the 'images' folder.")

@client.command()
async def audiotest(ctx, query: str):
    folder_path = os.path.join(os.getcwd(), 'audios')

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await ctx.send("The 'audios' folder does not exist in the same directory.")
        return

    allowed_extensions = ['.mp3', '.wav', '.ogg', '.flac']
    found_file = None

    for filename in os.listdir(folder_path):
        name_without_ext, ext = os.path.splitext(filename)
        if name_without_ext.lower() == query.lower() and ext.lower() in allowed_extensions:
            found_file = filename
            break

    if found_file:
        file_path = os.path.join(folder_path, found_file)
        file_to_attach = discord.File(file_path)
        await ctx.send(files=[file_to_attach])
    else:
        await ctx.send(f"No file found matching '{query}' with an allowed audio extension (.mp3, .wav, .ogg, .flac) in the 'audios' folder.")

client.run(token=token)
