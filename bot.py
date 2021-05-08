import discord
from discord.ext import commands, tasks
import requests
import json
from discord.utils import get

import vk_api
from youtube_search import YoutubeSearch

bot = commands.Bot(command_prefix='>')
bot.remove_command("help")

file_cfg = open("token.json")
cfg = json.load(file_cfg)
file_cfg.close()

bot.groups = ['-183416023', '-179926480', '-152424758', '-182044990']

bot.cat_house = ''

bot.nekoarchive_previous_link = ''
bot.nekoarchive_arr = []

bot.nekochan_previous_link = ''
bot.nekochan_heart_arr = []

bot.nekochan_meow = ''
bot.nekochan_meow_arr = []

bot.meduza_text = ''

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Самый базированный бот"))
    print(bot.user.name, "в сети!")

@tasks.loop(hours=1)
async def neko():
    # cat house
    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -183416023, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()
    image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
    image = image[1:-1]

    channel = bot.get_channel(839250460522577940)
    
    if bot.cat_house == '':
        bot.cat_house = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))
    elif bot.cat_house == image:
        pass
    elif bot.cat_house != image:
        bot.cat_house = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))
    
    # nekoarchive
    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -179926480, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()
    image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
    image = image[1:-1]

    if len(data["response"]["items"][1]["attachments"]) > 1:
        if len(bot.nekoarchive_arr) == 0:
            for i in data["response"]["items"][1]["attachments"]:
                bot.nekoarchive_arr.append(i["photo"]["sizes"][-1]["url"])

            for i in bot.nekoarchive_arr:
                message = await channel.send(i)
                await message.add_reaction(bot.get_emoji(839961477737349150))

        elif len(bot.nekoarchive_arr) > 0:
            current_arr = []

            for i in data["response"]["items"][1]["attachments"]:
                current_arr.append(i["photo"]["sizes"][-1]["url"])

            if current_arr == bot.nekoarchive_arr:
                pass
            else:
                bot.nekoarchive_arr = current_arr
                for i in bot.nekoarchive_arr:
                    message = await channel.send(i)
                    await message.add_reaction(bot.get_emoji(839961477737349150))
    else:

        image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
        image = image[1:-1]

        if bot.nekoarchive_previous_link == '':
            bot.nekoarchive_previous_link = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))
        elif bot.nekoarchive_previous_link == image:
            pass
        elif bot.nekoarchive_previous_link != image:
            bot.nekoarchive_previous_link = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))

    # nekochan <3
    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -152424758, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()

    if len(data["response"]["items"][1]["attachments"]) > 1:
        if len(bot.nekochan_heart_arr) == 0:
            for i in data["response"]["items"][1]["attachments"]:
                bot.nekochan_heart_arr.append(i["photo"]["sizes"][-1]["url"])

            for i in bot.nekochan_heart_arr:
                message = await channel.send(i)
                await message.add_reaction(bot.get_emoji(839961477737349150))

        elif len(bot.nekochan_heart_arr) > 0:
            current_arr = []

            for i in data["response"]["items"][1]["attachments"]:
                current_arr.append(i["photo"]["sizes"][-1]["url"])

            if current_arr == bot.nekochan_heart_arr:
                pass
            else:
                bot.nekochan_heart_arr = current_arr
                for i in bot.nekochan_heart_arr:
                    message = await channel.send(i)
                    await message.add_reaction(bot.get_emoji(839961477737349150))
    else:

        image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
        image = image[1:-1]

        if bot.nekochan_previous_link == '':
            bot.nekochan_previous_link = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))
        elif bot.nekochan_previous_link == image:
            pass
        elif bot.nekochan_previous_link != image:
            bot.nekochan_previous_link = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))

    # -182044990 nekochan_meow

    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -182044990, "count": 1, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()

    if len(data["response"]["items"][0]["attachments"]) > 1:
        if len(bot.nekochan_meow_arr) == 0:
            for i in data["response"]["items"][0]["attachments"]:
                bot.nekochan_meow_arr.append(i["photo"]["sizes"][-1]["url"])

            for i in bot.nekochan_meow_arr:
                message = await channel.send(i)
                await message.add_reaction(bot.get_emoji(839961477737349150))

        elif len(bot.nekochan_meow_arr) > 0:
            current_arr = []

            for i in data["response"]["items"][0]["attachments"]:
                current_arr.append(i["photo"]["sizes"][-1]["url"])

            if current_arr == bot.nekochan_meow_arr:
                pass
            else:
                bot.nekochan_meow_arr = current_arr
                for i in bot.nekochan_meow_arr:
                    message = await channel.send(i)
                    await message.add_reaction(bot.get_emoji(839961477737349150))
    else:

        image = json.dumps(data["response"]["items"][0]["attachments"][0]["photo"]["sizes"][-1]["url"])
        image = image[1:-1]

        if bot.nekochan_meow == '':
            bot.nekochan_meow = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))
        elif bot.nekochan_meow == image:
            pass
        elif bot.nekochan_meow != image:
            bot.nekochan_meow = image
            message = await channel.send(image)
            await message.add_reaction(bot.get_emoji(839961477737349150))


@tasks.loop(hours=1)
async def meduza():

    # https://vk.com/neural_meduza

    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -198361544, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    channel = bot.get_channel(839231157870526524)

    data = r.json()

    news = json.dumps(data["response"]["items"][1]["text"], ensure_ascii=False)
    news = news[1:-1]

    if bot.meduza_text == '':
        bot.meduza_text = news
        message = await channel.send(news)
        await message.add_reaction(👍)
        await message.add_reaction(👎)

    elif bot.meduza_text == news:
        pass
    elif bot.meduza_text != news:
        bot.meduza_text = news
        message = await channel.send(news)
        await message.add_reaction(👍)
        await message.add_reaction(👎)

@neko.before_loop
async def nekosent():
    await bot.wait_until_ready()
    print("Neko sent!")

@meduza.before_loop
async def newssent():
    await bot.wait_until_ready()
    print("News sent!")

# (aliases = ["p", "pl", "play"])
@bot.command()
async def yt(ctx, *, query = None):
    if query:
        await ctx.send(f"Идёт поиск по запросу {query}...")
        r = YoutubeSearch(query, max_results = 1).to_dict()
        await ctx.send("https://youtube.com" + r[0]["url_suffix"])
    else:
        await ctx.send("Укажите запрос!")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} зашёл на сервер {member.joined_at}')

if __name__ == "__main__":

    meduza.start()
    neko.start()
    bot.run(cfg["token"])
