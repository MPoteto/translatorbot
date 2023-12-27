
TOKEN = "null"

from googletrans import Translator
from langdetect import detect
import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="!", intents=discord.Intents().all())
bot.remove_command('help')

translator=False

@bot.event
async def on_ready():
    print("Бот работает")

def translate_text(text):
    translator = Translator()
    language = detect(text)
    if language == 'ru' or language == 'mk':
        translated = translator.translate(text, src='ru', dest='en')
    else:
        translated = translator.translate(text, src=language, dest='ru')
    return translated.text

@bot.event
async def on_message(message):
    global translator
    if message.content == "$translator" and message.author.bot == False:
        if message.author.guild_permissions.administrator:
            if translator == False:
                translator=True
                await message.reply("Перевод включен")
            elif translator == True:
                translator=False
                await message.reply("Перевод выключен")
    elif message.author.bot == False and translator == True:
        await message.reply(embed=discord.Embed(title="", description=translate_text(message.content), colour=0x2ecc71).set_footer(icon_url=message.author.avatar, text=f"Sent by {message.author.name}"))
try:
    bot.run(TOKEN)
except:
    print("Упс! Токен не валидный, измените в этом файле \"null\" на ваш токен")
    input()
