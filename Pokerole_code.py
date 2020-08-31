#------------------------------------------------------------------------------
#BOT CODE -- For  easy use in python-based discord bots
#Keep in mind you'll need the .csv files in the same location as the bot
#--------------------------Fresh Setup---------------------------------------------
#
#import csv
#import discord
#from discord.ext import commands
#
###put your bot's discord token here
#token = ''
###what prefix you want to use to call the bot
#prefix = '!'
#bot = commands.Bot(command_prefix = prefix)
#
#@bot.event
#async def on_ready():
#   print(f'{bot.user} has connected to Discord!')
####next line goes at the very bottom
#bot.run(token)
#
#######

#---------------------------Items---------------------------
pkmnItems = dict()

async def instantiateItemList():
    with open('PokeRoleItems.csv', 'r', encoding = "WINDOWS-1252") as file:
        reader = csv.reader(file)
        for row in reader:
            pkmnItems.update({row[0]:[row[1], row[13]]})
        pkmnItems.pop('Name')

async def pkmnitemhelper(item):
    if len(pkmnItems.keys()) == 0:
        await instantiateItemList()
    return pkmnItems[item.title()]

@bot.command(name = 'item', help = 'List an item\'s traits')
async def pkmn_search(ctx, *, itemname):
    try:
        found = await pkmnitemhelper(itemname.strip().title())

        output = f'__{itemname.title()}__\n'
        if found[1] != '':
            output += f'**Pokemon**: {", ".join(found[1])}\n'
        output += f'**Description**: {found[0].capitalize()}'

        await ctx.send(output)
    except:
        await ctx.send(f'{itemname} wasn\'t found in the item list.')

#---------------------------Moves---------------------------
pkmnMoves = dict()

async def instantiatePkmnMoveList():
    with open('pokeMoveSorted.csv', 'r', newline = '', encoding = "WINDOWS-1252") as infile:
        reader = csv.reader(infile)
        for row in reader:
            pkmnMoves.update({row[0]: row[1:]})

@bot.command(name = 'pkmnmove', help = 'List a pokemon move traits')
async def pkmn_search(ctx, *, term):
    if len(pkmnMoves.keys()) == 0:
        await instantiatePkmnMoveList()
    try:
        found = pkmnMoves[term.title()]

        output = f'__{term.title()}__\n'
        output += f'**Type**: {found[0].capitalize()}'
        output += f' -- **{found[1].capitalize()}**\n'
        output += f'**Target**: {found[7]}'
        output += f' -- **Power**: {found[2]}\n'
        output += f'**Dmg Mods**: {(found[3] or "None")} + {(found[4] or "None")}\n'
        output += f'**Acc Mods**: {(found[5] or "None")} + {(found[6] or "None")}\n'
        output += f'**Effect**: {found[8]}'

        await ctx.send(output)
    except:
        await ctx.send(f'{term} wasn\'t found in the move list.')

#---------------------------Stats---------------------------
pkmnStats = dict()

async def instantiatePkmnStatList():
    with open('PokeroleStats.csv', 'r', newline = '', encoding = "WINDOWS-1252") as infile:
        reader = csv.reader(infile)
        for row in reader:
            pkmnStats.update({row[1]: [row[0]] + row[2:]})

@bot.command(name = 'pkmnstats', help = 'List a pokemon\'s stats')
async def pkmn_search(ctx, *, term):
    if len(pkmnStats.keys()) == 0:
        await instantiatePkmnStatList()
    try:
        found = pkmnStats[term.title()]

        output = f'{found[0]} __{term.title()}__\n'
        output += f'**Rank**: {found[20]}\n'
        output += f'**Type**: {found[1].capitalize()}'
        if found[2] == '':
            output += '\n'
        else:
            output += f' / {found[2].capitalize()}\n'
        output += f'**Base HP**: {found[3]}\n'
        output += f'**Strength**: {found[4]} ({found[5]})\n'
        output += f'**Dexterity**: {found[6]} ({found[7]})\n'
        output += f'**Vitality**: {found[8]} ({found[9]})\n'
        output += f'**Special**: {found[10]} ({found[11]})\n'
        output += f'**Insight**: {found[12]} ({found[13]})\n'
        output += f'**Ability**: {found[14]}'
        if found[15] != '': #secondary
            output += f' / {found[15]}'
        if found[16] != '': #hidden
            output += f' ({found[16]})'
        if found[17] != '': #event
            output += f' <{found[17]}>'
        output += '\n'
        output += f'**Can Evolve**: {(found[18] or "No")}\n'
        output += f'**Other Forms**: {(found[19] or "No")}\n'

        await ctx.send(output)
    except:
        await ctx.send(f'{term} wasn\'t found in the pokemon list.')

#---------------------------Learn---------------------------
pkmnLearns = dict()

async def instantiatePkmnLearnsList():
    with open('PokeLearnMovesGens1to6.csv', 'r', newline = '', encoding = "WINDOWS-1252") as infile:
        reader = csv.reader(infile)
        for row in reader:
            pkmnLearns.update({row[0][4:]: row[1:]})

@bot.command(name = 'pkmnlearns', help = 'Lists what moves a pokemon can learn')
async def pkmn_search(ctx, *, term):
    if len(pkmnLearns.keys()) == 0:
        await instantiatePkmnLearnsList()
    try:
        found = pkmnLearns[term.title()]

        output = f'__{term.title()}__\n'
        moves = dict()
        for x in range(0,len(found),2):
            if found[x+1] not in moves:
                moves[found[x+1]] = [found[x]]
            else:
                moves[found[x+1]].append(found[x])

        for x in moves.keys():
            output += f'**{x}**\n'+'  |  '.join(moves[x]) + '\n'

        await ctx.send(output)
    except:
        await ctx.send(f'{term} wasn\'t found in the pokeLearns list.')