import googletrans
from googletrans import Translator 
import discord 
from discord.ext import commands
from keep_alive import keep_alive
import datetime


client = commands.Bot(command_prefix="*")

intents=intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

intents = discord.Intents(
messages=True, guilds=True, reactions=True, members=True)

TOKEN = "TOKEN" #TOKENİ KOY 

client.remove_command('help')

@client.event
async def on_ready():
    print("cryoncs")  #KONSOLO YAZDIRIYOR DEGISTIRRISIN

@client.command()
async def translate(ctx, lang, *,args):
    t = Translator()
    a = t.translate(args, dest=lang)
    embed=discord.Embed(title="Translated the text.", description=a.text, color=0x2b48b1) #DOKUNMA BURAYA
    embed.set_author(name=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}") #KAFANA GÖRE TAKIL BURA
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/810495626612965376/812237976909905950/indir.png") #RESMİ DEĞİŞTİR 
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    
    




@client.command()
async def help(ctx):
    embed=discord.Embed(title="Translate for Discord ", url="https://discordbotlist.com/bots/translator-for-discord/upvote", description="How to use ", color=0x0400ff) #BURASI BOTUN ACIKLAMASI KAFANA GORE TAKIL YİNE
    embed.set_image(url="https://cdn.discordapp.com/attachments/810495626612965376/812248814269759498/indir.png")
    embed.add_field(name="*translate (abbreviation of the language) (text) ", value="*translate german hello!", inline=True)
    await ctx.send(embed=embed)


@translate.error
async def translate_error(ctx, error):  #BURADA ADAM ERROR ALINCA ADAMA BUNU ATICAK ALDIGI ERROR FARKETMEZ 
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(color=0xacbdfb)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/810495626612965376/812237976909905950/indir.png") ,embed.add_field(name="If you want to use this command, first ``*translate`` , then your ``language`` you want to translate, finally your message example:", value="*translate **tr** Who is the best translator on Discord ",inline=True)
    await ctx.reply(embed=embed)



client.run("TOKEN")



