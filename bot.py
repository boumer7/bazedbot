import discord
from discord.ext import commands, tasks
import requests
import json
from discord.utils import get

from youtube_search import YoutubeSearch

from urllib.parse import urlparse, parse_qs

bot = commands.Bot(command_prefix='>')
bot.remove_command("help")

file_cfg = open("token.json")
cfg = json.load(file_cfg)
file_cfg.close()

bot.meduza_text = ''
bot.offset = 300

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Самый базированный бот"))
    print(bot.user.name, "в сети!")

@tasks.loop(seconds = 30)
async def neko(ctx):
    # cat house
    r = requests.get("https://api.vk.com/method/photos.get", 
    params = {"owner_id": -21674355, "album_id": "wall", "count": 10, "offset": bot.offset,
    "access_token": cfg["vk_token"], "v": "5.130"})

    if r:
        data = r.json()
        with open('data.json', 'w', encoding = 'utf-8') as fl:
            json.dump(data, fl, indent = 4, ensure_ascii= False)

    # channel = bot.get_channel(839250460522577940)
    
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

#@neko.before_loop
#async def nekosent():
#    await bot.wait_until_ready()
#    print("Neko sent!")

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
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
        if query.path[:9] == '/playlist': return parse_qs(query.query)['list'][0]

    return None

@bot.command(aliases=['комната', 'room', 'nr', 'w2g', 'watch2gether'])
async def newroom(ctx, *, yt_url = None):

    vid_id = await video_id(yt_url)

    if yt_url:

        if vid_id:
            r = requests.post('https://w2g.tv/rooms/create.json', 
            json = {
            "w2g_api_key": cfg["w2g"],
            "share": yt_url,
            "bg_color": "#EC1622",
            "bg_opacity": "50"})

            if r:
                streamkey = r.json()["streamkey"]
                room_link = f"https://w2g.tv/rooms/{streamkey}"

                w2g_embed = discord.Embed(title="Ваша комната в Watch2Gether создана!", color=0xec1622)
                w2g_embed.add_field(name="Комната", value=f'[Перейти]({room_link})', inline=False)
                w2g_embed.set_image(url = f"https://img.youtube.com/vi/{vid_id}/0.jpg")   
                await ctx.send(embed=w2g_embed)
            else:
                await ctx.send(f"Ошибка запроса: {r.status_code}")

        else:
            r = requests.post('https://w2g.tv/rooms/create.json', 
            json = {
            "w2g_api_key": cfg["w2g"],
            "share": yt_url,
            "bg_color": "#EC1622",
            "bg_opacity": "50"})

            if r:
                streamkey = r.json()["streamkey"]
                room_link = f"https://w2g.tv/rooms/{streamkey}"

                w2g_embed = discord.Embed(title="Ваша комната в Watch2Gether создана!", color=0xec1622)
                w2g_embed.add_field(name="Комната", value=f'[Перейти]({room_link})', inline=False)
                await ctx.send(embed=w2g_embed)
            else:
                await ctx.send(f"Ошибка запроса: {r.status_code}")

        
    else:
        await ctx.send("Введите запрос для Watch2Gether. Поддерживаемые сервисы.")

if __name__ == "__main__":

    # meduza.start()
    # neko.start()
    bot.run(cfg["token"])
