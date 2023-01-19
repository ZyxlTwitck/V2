"""
 ________      ___    ___      ________      ___    ___ ___    ___  ___          
|\   __  \    |\  \  /  /|    |\_____  \    |\  \  /  /|\  \  /  /||\  \         
\ \  \|\ /_   \ \  \/  / /     \|___/  /|   \ \  \/  / | \  \/  / |  \  \        
 \ \   __  \   \ \    / /          /  / /    \ \    / / \ \    / /    \  \       
  \ \  \|\  \   \/  /  /          /  /_/__    \/  /  /   /     \/      \  \_______  
   \ \_______\__/  / /           |\________\__/  / /    /  /\   \  		\|________|
    \|_______|\___/ /             \|_______|\___/ /    /__/ /\ __\    
             \|___|/                       \|___|/     |__|/ \|__|                        
"""

try:
	import discord, colorama, requests, math, random, asyncio, pyfiglet
	from discord.ext import commands
	from discord.ext.commands.core import command
	from discord import utils
	from colorama import Fore
	import config
	from test import number
except ImportError:
    input ("If you not install the requirements.txt -- Will not work! [ *Press enter to start* ]:")

ascii_banner = pyfiglet.figlet_format("By Zyxl")
print(ascii_banner)

channelIDS = 1015684903435776082

client = commands.Bot(command_prefix = '.', intents = discord.Intents.all(), case_insensitive=True)
client.remove_command("help")
# .hello
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all(), case_insensitive=True)
client.remove_command("help")

# def progress_bar1 #
#def progress_bar1( progress,total,color=colorama.Fore.YELLOW ):
    #percent = 100 * (progress / float (total))
    #bar = '█' * int (percent) + '-' * (100 - int (percent))
    #print (color + f"\r|{bar}| {percent:.2f}%",end="\r")
    #if progress == total:
        #print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%",end="\r")

#numbers1 = [x * 5 for x in range (3000,3500)]
#results1 = []

# progress_bar1 #
#progress_bar1 (0,len (numbers1))
#for i,x in enumerate (numbers1):
    #results1.append (math.factorial (x))
    #progress_bar1 (i + 1,len (numbers1))

#print (colorama.Fore.RESET)

#print(' ')

@client.event

async def on_ready():
	print(' ')
	print(' ')
	print('[MODER] - ⚡Zyxl⚡ = Bot - Successfully Logged in system DISCORD SERVER!')

@client.event
async def on_member_join(member):
	print(f"{member} has joined!")
	await client.get_channel(1015684903435776082).send("Добро пожаловать в "+"***{}***, Прочитайте правила сервера в канале ruls".format(member.guild.name)+" "+"{}".format(member.mention))

@client.event
async def on_member_remove(member):
	print(f"{member} leave the server!")
	await client.get_channel(1015684903435776082).send("Вышёл из сервера "+"***{}***".format(member.guild.name)+" "+"{}".format(member.mention))


#@client.event
#async def on_member_join(member):
  	#print(f"{member} has joined!")

@client.command(pass_context = True)

async def hello(ctx):
	await ctx.send('Welcome, to the Zyxl - TEAM')

@client.command(pass_context = True)

async def link(ctx):
	await ctx.send('https://github.com/Zyxal-dev')

@client.command(pass_context = True)

async def lua1(ctx):
	await ctx.send('''


	--------------------- [LUA1] WAS SENDED! ---------------------


	--BROUGHT TO YOU BY ROBLOXSCRIPTS.NET!--

loadstring(game:HttpGet("https://raw.githubusercontent.com/UltraStuff/scripts2/main/bf", true))()

code KRNL : 5e76578f510abb3263f578a8bc95fe98

--NEW - SCRIPT - FOR - BLOX FRUITS - Zyxl--

loadstring(game:HttpGet("https://raw.githubusercontent.com/hajibeza/RIPPER-HUB/main/BFV2.lua"))()

--Second - Script - FOR - BLOX FRUITS--

_G.Beta = true
loadstring(game:HttpGet"https://raw.githubusercontent.com/xQuartyx/DonateMe/main/ScriptLoader")()

--NEW - 11/4/2022 -- BLOX FRUITS--

loadstring(game:HttpGet("https://raw.githubusercontent.com/RimuruScripter/ZamaHub/main/OnlyPc"))()''')

@client.command(pass_context = True)

async def lua2(ctx):
	await ctx.send('''
	
	--------------------- [LUA2] WAS SENDED! 19/12/2022 update - mobile  ---------------------
	
	loadstring(game:HttpGet("https://raw.githubusercontent.com/Fiend1sh/FiendMain/main/FiendMainLoader", true))()''')

@client.command(pass_context = True)

async def mbapk(ctx):
	await ctx.send('''
	
	--------------------- 19/12/2022 update - mobile EXECUTER ---------------------
	
	https://www.mediafire.com/file/ez97wdzl7zlr5us/Hydrogen-1.0.5-Alpha.apk/file''')

@client.command(pass_context = True)

async def statsevent(ctx):
	await ctx.send('Пашёл нахуй (заебал уже!)')

@client.command(pass_context = True)

async def startevent(ctx):
	await ctx.send('Хочешь Чит на Стандофф 2 [ZyxlCheats] ❌')

@client.command(pass_context = True)

async def checkacc(ctx):
	await ctx.send('Roblox: Account = [AaronMakrl] = [🔒Banned🔒]')

@client.command(pass_context = True)
async def clear(ctx, amount=10):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'Удалено {amount} сообщений!', delete_after = 3)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}', delete_after = 3)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}', delete_after = 3)

# Connect
token = open('token.txt', 'r').readline()

client.run(token)

#intents = discord.Intents.default()
#intents.message_content = True
#, intents=intents

#@client.command(pass_context = True)

#async def hello(ctx):
	#await ctx.send('Welcome, to the Zyxal - GROUP')

#@client.command(pass_context = True)

#async def link(ctx):
	#await ctx.send('https://github.com/Zyxal-dev')