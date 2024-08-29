import discord
from discord.ext import commands
from datetime import timedelta
from discord import FFmpegPCMAudio
from discord.ext.commands import bot

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#SettarBotMessage
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
    elif message.content.lower().startswith(''):
        await message.channel.send('')
            

    await bot.process_commands(message)

#SettarBotTimeout
@bot.command(name="Any command name of your choice")
@commands.has_permissions(moderate_members=True)
async def command_name (ctx, member: discord.Member, duration: int, *, reason=None):
    try:
        timeout_duration = timedelta(seconds=duration)

        await member.timeout(timeout_duration, reason=reason)

        await ctx.send(f"{member.mention} muted for {duration} seconds. Reason: {reason}")

    except discord.Forbidden:
        await ctx.send('I do not have permission')
        print("Permission error: Forbidden")

    except discord.HTTPException as e:
        await ctx.send(f"Error: {e}")
        print(f"HTTP Exception: {e}")

    except Exception as e:
        await ctx.send(f"Error: {e}")
        print(f"Unexpected Error: {e}")

#SettarBotVoiceChatAudioFiles
@bot.command(pass_context = True)
async def command_name (ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send('')
        voice = await channel.connect()
        source = FFmpegPCMAudio("A voice file")
        player = voice.play(source)
    else:
        await ctx.send('')

#SettarBotVoiceChatAudioFiles2
@bot.command(pass_context = True)
async def command_name (ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send('')
        voice = await channel.connect()
        source = FFmpegPCMAudio("A voice file")
        player = voice.play(source)
    else:
        await ctx.send('')

#SettarBotLeave
@bot.command(pass_context = True)
async def command_name(ctx):
    if (ctx.voice_client):
        channel = ctx.message.author.voice.channel
        await ctx.send('')
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('')
#SettarBotPersonalMessage
@bot.command()
async def command_name(ctx, user: discord.Member, *, message=None):
    if message is None:
        message = "Your message"
    embed = discord.Embed(title=message)
    try:
        await user.send(embed=embed)
        await ctx.send(f"{user.display_name}")
    except discord.Forbidden:
        await ctx.send('')
#SettarBotImage
@bot.command(pass_context = True)
async def command_name(ctx):
    await ctx.send(file=discord.File('Your image'))

token = "Your token"

bot.run(token)
