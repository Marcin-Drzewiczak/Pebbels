import discord
from discord.ext import commands
import random
import os


# Replace 'your-bot-token' with your bot's token
TOKEN = os.getenv('TOKEN')


# Define emotes
WHITE_PEBBLE = '⚪'
BLACK_PEBBLE = '⚫'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


# Custom help command
bot.remove_command('help')
@bot.command(name='help', help='Displays information on how to use the bot.')
async def help_command(ctx):
    help_text = '''
**Pebble Bot Commands:**

`!pebbles <white> <black> <draw>`
Draws a specified number of white and black pebbles from a bag.
- `<white>`: Number of white pebbles in the bag.
- `<black>`: Number of black pebbles in the bag.
- `<draw>`: Number of pebbles to draw from the bag.

`!roll <dice>`
Rolls specified number of dice with specified number of sides.
- `<dice>`: Dice notation, like `2d6` for two six-sided dice.

`!help`
Displays information on how to use the bot.
'''

    await ctx.send(help_text)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='pebbles', help='Draws specified amount of white and black pebbles from the bag.')
async def pebbles(ctx, white: int, black: int, draw: int):
    if draw > white + black:
        await ctx.send("You can't draw more pebbles than there are in the bag!")
        return

    bag = [WHITE_PEBBLE] * white + [BLACK_PEBBLE] * black
    random.shuffle(bag)
    drawn_pebbles = random.sample(bag, draw)

    white_drawn = drawn_pebbles.count(WHITE_PEBBLE)
    black_drawn = drawn_pebbles.count(BLACK_PEBBLE)

    result = f"{WHITE_PEBBLE}: {white_drawn} | {BLACK_PEBBLE}: {black_drawn}"
    await ctx.send(result)


@bot.command(name='roll', help='Rolls specified number of dice with specified number of sides (e.g. !roll 2d6).')
async def roll(ctx, dice: str):
    try:
        num_dice, num_sides = map(int, dice.split('d'))
    except ValueError:
        await ctx.send('Invalid format. Use NdS, where N is the number of dice and S is the number of sides (e.g. 2d6).')
        return

    if num_dice <= 0 or num_sides <= 0:
        await ctx.send('The number of dice and sides must be positive integers.')
        return

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    result = ', '.join(map(str, rolls))
    await ctx.send(f'You rolled: {result}')
bot.run(TOKEN)
