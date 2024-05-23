import requests
import random
import discord
from discord.ext import commands
from random import randint
from os import listdir
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    count_heh=int(count_heh)
    if count_heh<100:
        await ctx.send("he" * count_heh)
    else:
        await ctx.send("Çok fazla heh!")

@bot.command()
async def total(ctx,*args):
    total=0
    for num in args:
        total+=int(num)
    await ctx.send(total)

@bot.command()
async def math(ctx,process):
    await ctx.send(eval(process))
    """(12)*"""

@bot.command()
async def tahmin(ctx, s1=1, s2=100):

    dogru_sayi = random.randint(s1, s2)
    tahmin_hakki = 1 if (s2-s1) == 0 else (1 + (s2-s1).bit_length())

    await ctx.send(f"@{ctx.author} {s1} ile {s2} arasında bir sayı seçildi.")
    await ctx.send(f"@{ctx.author} {tahmin_hakki} tahmin hakkınız var")

    while tahmin_hakki > 0:
        tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        kullanici_tahmini = tahmin_mesaji.content

        try:
            kullanici_tahmini = int(kullanici_tahmini)
        except :
            await ctx.send(f"@{ctx.author} Lütfen bir sayı girin.")
            continue
        
        tahmin_hakki -= 1
        if kullanici_tahmini == dogru_sayi:
            await ctx.send(f"@{ctx.author} Bildiniz! Tebrikler!")
            break
        elif kullanici_tahmini < dogru_sayi:
            await ctx.send(f"@{ctx.author} Bilgisayarın tahmini daha büyük")
            await ctx.send(f"{tahmin_hakki} hakkınız kaldı")
        else:
            await ctx.send(f"@{ctx.author} Bilgisayarın tahmini daha küçük")
            await ctx.send(f"@{ctx.author} {tahmin_hakki} hakkınız kaldı")
    else:
        await ctx.send(f"@{ctx.author} Hak bitti, doğru cevap {dogru_sayi}")

@bot.command()
async def send_image(ctx):
    with open('C:/Users/HP/Documents/python/bots/bot2s/images/image1','rb') as f:
        picture=discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def send_random_image(ctx):
    image_dir=[listdir('C:/Users/HP/Documents/python/bots/bot2s/images/')]
    chance_list=[0.1,0.2,0.4,0.3]
    image_name=random.choices(image_dir,weights=chance_list)[0]
    with open(f'C:/Users/HP/Documents/python/bots/bot2s/images/{image_name}','rb') as f:
        picture=discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_pokemon_image_url(name): 
    url= f"https://pokeapi.co/api/v2/pokemon/{name}"
    res=requests.get(url)
    data=res.json()
    return data['sprites']['front_default']
def get_dog_image_url(): 
    url= f"https://random.dog/woof.json"
    res=requests.get(url)
    data=res.json()
    return data['url']
def get_fox_image_url(): 
    url= f"https://randomfox.ca/floof/"
    res=requests.get(url)
    data=res.json()
    return data['image']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('pokemon')
async def pokemon(ctx,name):
    try:
        image_url = get_pokemon_image_url(name)
        await ctx.send(image_url)
    except:
        await ctx.send("Bir hata oluştu veya pokemon kart bulunamadı!\nŞunları deneyin:\n-İnternet bağlantınızı kontrol edin\n-Pokemon kart adını düzgün yazın")
@bot.command("dog")
async def dog(ctx):
    try:
        image_url = get_dog_image_url()
        await ctx.send(image_url)
    except:
        await ctx.send("Bir hata oluştu!")
@bot.command("fox")
async def fox(ctx):
    try:
        image_url = get_fox_image_url()
        await ctx.send(image_url)
    except:
        await ctx.send("Bir hata oluştu!")

bot.run("MTIzNzgzOTAxNjgwODY3NzQwNw.GBpgmQ.LCxTcazA_OSQ7AExwJjmPrKOpDp3tGfGVNc-IY")
