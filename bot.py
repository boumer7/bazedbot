import discord
from discord.ext import commands, tasks
import requests
import json
from discord.utils import get

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

bot.nekomemes = ''
bot.onlyneko = ''
bot.nekotyanochki = ''

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

    #nekomemes

    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -198134349, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()
    image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
    image = image[1:-1]

    channel = bot.get_channel(839250460522577940)
    
    if bot.nekomemes == '':
        bot.nekomemes = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))
    elif bot.nekomemes == image:
        pass
    elif bot.nekomemes != image:
        bot.nekomemes = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))

    # onlyneko -202553134

    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -202553134, "count": 1, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()
    image = json.dumps(data["response"]["items"][0]["attachments"][0]["photo"]["sizes"][-1]["url"])
    image = image[1:-1]

    channel = bot.get_channel(839250460522577940)
    
    if bot.onlyneko == '':
        bot.onlyneko = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))
    elif bot.onlyneko == image:
        pass
    elif bot.onlyneko != image:
        bot.onlyneko = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))

    # https://vk.com/tyanochki_nyanochki -198356798

    r = requests.get("https://api.vk.com/method/wall.get", params = {"owner_id": -198356798, "count": 2, "offset": 0,
    "access_token": cfg["vk_token"], "v": "5.130"})

    data = r.json()
    image = json.dumps(data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][-1]["url"])
    image = image[1:-1]

    channel = bot.get_channel(839250460522577940)
    
    if bot.nekotyanochki == '':
        bot.nekotyanochki = image
        message = await channel.send(image)
        await message.add_reaction(bot.get_emoji(839961477737349150))
    elif bot.nekotyanochki == image:
        pass
    elif bot.nekotyanochki != image:
        bot.nekotyanochki = image
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
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')

    elif bot.meduza_text == news:
        pass
    elif bot.meduza_text != news:
        bot.meduza_text = news
        message = await channel.send(news)
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')

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
        await ctx.send("Укажите запрос")

@bot.command()
async def poll(ctx, *, poll_type = None):
    if poll_type:
        if poll_type == 'newtext':
            ctx.send("Голосование за создание нового текстового канала.")
        elif poll_type == 'newvoice':
            ctx.send("Голосование за создание нового голосового канала.")
        elif poll_type == 'report':
            ctx.send("Нарушил ли {user} пункт правил №{rule}?".format("пользователь", "правило"))
    else:
        await ctx.send("Укажите тип голосования. Для большей информации напишите **>help**")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} зашёл на сервер {member.joined_at}')

@bot.command()
async def help(ctx):
    help_embed = discord.Embed(title = "Команды", colour = 0xec1622)
    help_embed.add_field(name = ">poll newtext <название>", value = "Голосование за создание нового текстового канала", inline = False)
    help_embed.add_field(name = ">poll newvoice <название>", value = "Голосование за создание нового голосового канала", inline = False)
    help_embed.add_field(name = ">poll report @пользователь <пункт правил>", value = "Пожаловаться на нарушение правил сервера.", inline = False)
    help_embed.add_field(name = ">yt", value = "Поиск видео по запросу на YouTube", inline = False)
    await ctx.send(embed = help_embed)

@bot.command()
async def connect(ctx, *, channel: discord.VoiceChannel=None):

    if not channel:
        try:
            channel = ctx.author.voice.channel

        except:
            await ctx.send("Чтобы я зашёл в голосовой канал, для начала должны зайти вы.")

    vc = ctx.voice_client

    if vc:
        if vc.channel.id == channel.id:
            return
        try:
            connection = await vc.move_to(channel)
            if connection:
                await ctx.send("Я успешно подключился.")
        except:
            pass
    
    else:
        try:
            connection = await channel.connect()
            if connection:
                await ctx.send("Я успешно подключился.")
        except:
            pass

@bot.command()
async def leave(ctx):
    vc = ctx.voice_client

    if not vc or not vc.is_connected():
        await ctx.send("Я не нахожусь в голосовом канале")

    else:
        await vc.disconnect()
        await ctx.send("Я успешно отключился.")

@bot.command(aliases=['дополнить', 'продолжить', 'continue', 'con', 'porfirevich'])
async def porf(ctx, *, req = None):
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '50',
    'Content-Type': 'text/plain;charset=UTF-8',
    'dnt': '1',
    'Host': 'pelevin.gpt.dobro.ai',
    'Origin': 'https://porfirevich.ru',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'sec-gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    if req:
        r = requests.post('https://pelevin.gpt.dobro.ai/generate/', json = {"prompt": req, "length":30}, headers = headers)
        if r:
            for i in range(3):
                await ctx.send(f"{req}{r.json()['replies'][i]}")
        else:
            await ctx.send(f'Слишком много запросов: {r.status_code}')
    else:
        await ctx.send("Введите запрос")

async def video_id(url):
    if 'youtube.com' in url or 'youtu.be' in url:
            return url[-11:-1]
    return None

@bot.command(aliases=['комната', 'room', 'nr', 'w2g', 'watch2gether'])
async def newroom(ctx, *, yt_url = None):

    vid_id = await video_id(yt_url)

    if yt_url and vid_id:
        r = requests.post('https://w2g.tv/rooms/create.json', 
        json = {
        "w2g_api_key": cfg["w2g"],
        "share": yt_url,
        "bg_color": "#EC1622",
        "bg_opacity": "50"})

        if r:
            streamkey = r.json()["streamkey"]
            room_link = f"https://w2g.tv/rooms/{streamkey}"

            w2g_embed = discord.Embed(title="Ваша комнате создана!", color=0xec1622)
            w2g_embed.add_field(name="Комната", value=f'[Перейти]({room_link})', inline=False)
            w2g_embed.set_image(url = f"http://img.youtube.com/vi/{vid_id}/hqdefault.jpg")   
            await ctx.send(embed=w2g_embed)
        else:
            await ctx.send(f"Ошибка запроса: {r.status_code}")
    else:
        await ctx.send("Введите ссылку на YouTube")

if __name__ == "__main__":

    # meduza.start()
    # neko.start()
    bot.run(cfg["token"])
