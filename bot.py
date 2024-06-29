# бот, который считает, сколько разлагается вещь

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# код
items = {
    'пластик': 450,
    'стекло': 'неразлагаемое',
    'полиэтилен': 20, 
    'алюминий': 318, 
    'подгузник': 500
}

@bot.command()
async def howlong(ctx, item):
    item = item.lower()
    if item in items.keys():
        await ctx.send(f'Вещь {item} разлагается {items[item]} лет')
    else:
        await ctx.send('Такой вещи нет в базе данных')

# бот, который дает советы по экологии
@bot.command()
async def eco(ctx):
    facts = [
        "Каждый год в океаны попадает около 8 миллионов тонн пластика.",
        "Леса покрывают около 30% поверхности земли и являются домом для 80% наземных видов животных и растений.",
        "Более миллиарда людей живут без доступа к чистой питьевой воде.",
        "Один рециклированный стеклянный бутыль экономит достаточно энергии, чтобы запитать лампу на 4 часа.",
        "Каждое сохраненное дерево может поглотить около 21 кг углекислого газа в год."
    ]
    await ctx.send(f'Рандомный факт: {random.choice(facts)}')
    

bot.run('ТОКЕН')
