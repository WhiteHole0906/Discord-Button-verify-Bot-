import discord
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button
import random
import asyncio
from discord.utils import get

bot = Bot(command_prefix = ".") #명령어 앞에 prefix 맘대로 설정 가능함

bot.remove_command('help')

token = '봇토큰' #봇토큰

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"{bot.user}로 로그인이 성공적으로 되셨습니다!")

@bot.command()
async def 인증(ctx):
    try:
        member = ctx.message.author

        rol = discord.utils.get(ctx.guild.roles, name="❤역할이름❤") #수정해야함
        if rol in member.roles:
            pass
        else:
            def check(res):
                return ctx.author == res.user and res.channel == ctx.channel 
        
            emojis = ["💌", "🎶", "🥰", "💀", "🚫", "🔞", "👏", "✅", "✝", "⭕", "☢", "😆", "😑", "😊", "🎁", "🤣", "😂", "🍙", "🧨", "🎫", "🥽", "✨", "🎇", "🎆", "🎈", "🎃", "🎉", "🧧"]
            a = random.choice(emojis)
            b = random.choice(emojis)
            ran = random.randint(1, 2)
            while a == b:
                a = random.choice(emojis)
                b = random.choice(emojis)
            if ran == 1:
                asdf = a
                asdf2 = b
            if ran == 2:
                asdf = b
                asdf2 = a
            embed = discord.Embed(title='🌍 서버 인증하기', description=f'이 버튼을 10초 안에 눌러주세요. (Made BY WhiteHole) ({a})', colour=discord.Colour.blue())
            embed2 = discord.Embed(title='✅ 인증성공', description=f'{ctx.author.mention}, 3초 뒤 역할이 지급됩니다. (Made BY WhiteHole) ', colour=discord.Colour.green())
            embed3 = discord.Embed(title='⛔ 인증실패', description=f'{ctx.author.mention}, 버튼이 잘못되었습니다 다시 시도해주세요. (Made BY WhiteHole) ', colour=discord.Colour.red())
            embed4 = discord.Embed(title='⛔ 인증실패', description=f'{ctx.author.mention}, 시간 초과입니다. 다시 시도해주세요. (Made BY WhiteHole)', colour=discord.Colour.red())

            await ctx.send(
                embed=embed,
                components = [
                    Button(style = 1, label = asdf), Button(style = 3, label = asdf2)
                ]
            )

            res = await bot.wait_for("button_click", check = check, timeout=10) #몇초 안에 누르느냐 (이것또한 수정가능 현재 10초로 설정되있음.)
            u = res.component.label

            if u == a:
                await res.respond(embed = embed2)
                await asyncio.sleep(3)
                await ctx.channel.purge(limit=2)
                await member.add_roles(rol)
            elif u == b:
                await res.respond(embed = embed3)
                await asyncio.sleep(3)
                await ctx.channel.purge(limit=2)

    except:
        await ctx.channel.purge(limit=2)
        await ctx.send(embed=embed4)
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)


bot.run(token)
