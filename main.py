import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print (f"Has iniciado sesion como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "/img tung tung":
        with open('tung-tung-tung-sahur-v0-eDFwaGRqYzNheW9lMWarK4b-9D-MyRL7fRrH2ixm_5zZdrITDVRXBLPvLSEX.webp', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Nunca me gustaro neste tipo de memes...", file = picture)

    if message.content.lower() == "/img island":
        with open('r_2819074_9yP3u.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Basicamente, esta mandando un mensaje de ayuda con codigo, (espero que no le tome mucho escribirlo todo jeje)", file = picture)

    if message.content.lower() == "/img yoda":
        with open('8qh67g.webp', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Estudiar codigo tu debes... Creo que no debo explicar mucho aqui.", file = picture)
            
    if message.content.lower() == "/img weapon":
        with open('images.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Elige sabiamente, cada una es diferente y se usa para lo suyo, phyton es mas facil de controlar, java mas dificil pero mas util...", file = picture)
    if message.content.lower() == "/img programmer_baby":
        with open('Programmer-baby.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Siempre las pruebas de programacion o como se inicia es con print:('hello world').", file = picture)
    if message.content.lower() == "/img homelander":
        with open('WhatsApp Image 2025-05-16 at 15.57.43_c6179fd8.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Es un bot que resuelve automaticamente los errores, y el lo esta usando a su antojo :).", file = picture)

    if message.content.lower() == "/img bug2":
        with open('1_KcQUEkOQ1LoMDHkMZ-Yymw.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Cuando profin sabes como resolver ese bug pero ya es tarde :/.", file = picture)

    if message.content.lower() == "/img bug1":
        with open('hq720.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="No hay codigo en esa parte, por lo tanto es confusa la razon del bug, un fantasma?", file = picture)

    if message.content.lower() == "/img cry_guy":
        with open('unnamed.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content=":(", file = picture)
    
    if message.content.lower() == "/img obi-wan":
        with open('Q_jQKTk88F6ouuVzLOQmP8wqp-1NuuxVNBf8MNVIAsI.webp', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Hello there ;).", file = picture)

    if message.content.lower() == "$memes":
        await message.channel.send(content="Estos son los memes con los que aprenderas de su codigo, cada un con una descrpcion y explicacion!: /img tung_tung, /img obi-wan, /img cry_guy")\
        
    if message.content.lower() == "$code":
        await message.channel.send(content="Estos son los memes normales!: /img bug1, /img bug2, /img homelander, /img programmer_baby, /img weapon, /img yoda, /img island")     

bot.run("MTM2NTQzMTQ0MDc2MTk1MDM3MQ.GE_2Ft.80T2TwGwlO9AzmW2jnYHUKDOeOBjtmSo9tQnz4")
