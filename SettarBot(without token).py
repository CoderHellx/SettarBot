import discord
from discord.ext import commands
from datetime import timedelta
from discord import FFmpegPCMAudio
import requests
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
import os

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


    if message.content.lower().startswith("?nasılsın"):
        await message.channel.send('Kötü , konuşmaya çalıştığım 1237. kız beni terk etti.')
    elif message.content.lower().startswith("?yüzme nasıl"):
        await message.channel.send('İyi , Medipol %50 burs veriyor.')
    elif message.content.lower().startswith("?instanı alabilir miyim"):
        await message.channel.send('İnsta kapalı olmaz.')
    elif message.content.lower().startswith("?tiktokunu alabilir miyim"):
        await message.channel.send('olur tiktokum ---> https://www.tiktok.com/@yigit_evgulu')
    elif message.content.lower().startswith("?ytni alabilir miyim"):
        await message.channel.send('olur ytem ---> https://www.youtube.com/@yse9886')
    elif message.content.lower().startswith("?sag ol"):
        await message.channel.send('Sıkıntı yok bir daha gacı mevzusu aç yeter.')
    elif message.content.lower().startswith("?help"):
        await message.channel.send(
            "Anlık Komutlarım: \n1.?help(yardım)\n2.?nasılsın\n3.?yüzme nasıl\n4.?instanı alabilir miyim\n5.?tiktokunu alabilir miyim\n6.?ytni alabilir miyim")

    await bot.process_commands(message)

#SettarBotTimeout
@bot.command(name="ssh")
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, duration: int, *, reason=None):
    try:
        timeout_duration = timedelta(seconds=duration)

        await member.timeout(timeout_duration, reason=reason)

        await ctx.send(f"{member.mention} susturuldu {duration} saniye boyunca. Sebep: {reason}")

    except discord.Forbidden:
        await ctx.send("Yetkim yok")
        print("Permission error: Forbidden")

    except discord.HTTPException as e:
        await ctx.send(f"Hata: {e}")
        print(f"HTTP Exception: {e}")

    except Exception as e:
        await ctx.send(f"Hata: {e}")
        print(f"Unexpected Error: {e}")

@bot.command(pass_context = True)
async def rr (ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await ctx.send("Geliyorum Gacılar!!!")
        voice = await channel.connect()
        source = FFmpegPCMAudio("Rick-Roll-Sound-Effect.wav")
        player = voice.play(source)
    else:
        await ctx.send("Bu komutun çalışması için benim bir sesli sohbette olmam lazım.")

#SettarBotJoinandLeave
@bot.command(pass_context = True)
async def çık(ctx):
    if (ctx.voice_client):
        channel = ctx.message.author.voice.channel
        await ctx.send("Gacı Yokmus Ya")
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Bu komutun çalışması için benim bir sesli sohbette olmam lazım.")

@bot.command()
async def sex(ctx, user: discord.Member, *, message=None):
    if message is None:
        message = "Saat? , Mekan?"
    embed = discord.Embed(title=message)
    try:
        await user.send(embed=embed)
        await ctx.send(f"{user.display_name} halledildi __--__ ")
    except discord.Forbidden:
        await ctx.send("Dm'si açık değil aptalın.")

token =

bot.run(token)
