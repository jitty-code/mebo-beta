import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='me!', help_command=None)

# commands

@bot.command()
async def say(ctx, *say: str):
  def string(s):
    str1 = ""
    for ele in s:
        str1 += ele
        str1 += " "
    return str1
  await ctx.send(string(say))

@bot.command()
async def hello_world(ctx):
    await ctx.send("Hello, World")


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms :ping_pong:')


@bot.command()
async def continuing(ctx):
    await ctx.send(f'...')


@bot.command()
async def channel_id(ctx, channel: discord.TextChannel):
    await ctx.send(f"Here's your mentioned channel ID: {channel.id}")
    

@bot.command()
async def test(ctx):
    await ctx.send("Test 1")
    await ctx.send("Test 2")
    await ctx.send("Test 3")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount + 1)
  
@bot.command()
async def mebo(ctx):
  await ctx.send("Is the best bot")
 
# --- help command ---
@bot.command()
async def help(ctx, type = ''):
  if type == 'Normal' or type == 'normal':
    embed=discord.Embed(title="Help Menu (Normal)", description="Write me! to run the commands", color=0xff0000)
    embed.add_field(name="Help", value="Shows this menu.", inline=False)
    embed.add_field(name="Ping", value="Shows the ping of the bot.", inline=False)
    embed.add_field(name="Say", value="Make the bot say something (Don't make it swear or kick).", inline=False)
    embed.add_field(name="Invite", value="Get an invite to invite the bot to your server.", inline=False)
    embed.add_field(name="Thank **YOU**", value="Thank **YOU** for using <@821727153803493416>, have fun!", inline=False)
    await ctx.send(embed=embed)


  elif type == 'Admin' or type == 'admin' or type == 'administrator' or 'Administrator':
    embed=discord.Embed(title="Help Menu (Admin)", description="Write me! to run the commands", color=0xff0000)
    embed.add_field(name="Ban", value="Bans a person", inline=False)
    embed.add_field(name="Unban", value="Unbans a person if already banned (ex. appealed_person#6009)", inline=False)
    embed.add_field(name="Kick", value="Kicks a person", inline=False)
    await ctx.send(embed=embed)


  elif type == 'Dev' or type == 'dev' or type == 'developer' or type == 'Developer':
    embed=discord.Embed(title="Help Menu (Dev)", description="Write me! to run the commands", color=0xff0000)
    embed.add_field(name="Test", value="Test command made for devs", inline=False)
    embed.add_field(name="hello_world", value="Sends \"Hello, World\" message.", inline=False)
    await ctx.send(embed=embed)


  else:
    embed=discord.Embed(title="Help Menu", description="Write me!help type to choose the page", color=0xff0000)
    embed.add_field(name="Normal", value="List of normal commands", inline=False)
    embed.add_field(name="Admin", value="List of admin commands", inline=False)
    embed.add_field(name="Dev", value="List of dev commands", inline=False)
    await ctx.send(embed=embed)

    
# --- moderation ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.member, *, reason=None):
  
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked {member}')


@bot.command()
async def invite(ctx):
    await ctx.send("Invite me to your server using this link:\nhttps://discord.com/api/oauth2/authorize?client_id=821727153803493416&permissions=3221748807&scope=bot")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  member_name, member_discriminator = member.split('#')
  banned_users = await ctx.guild.bans()

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
     
# --- events ---

@bot.event
async def on_ready():
    print("Mebo is ready!")

# --- error handling ---

@channel_id.error
async def channelId_err(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send("Please give the channel name.")

@say.error
async def say_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send("Hello, World!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("That is not a command :frowning:. Please contact <@713554958490009601> or anyone with the <@&822182707172737095> role.")

#error handler
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    ctx.send("you must send a argument")

@clear.error
async def clear_error(ctx, error):
  if isinstance (error, commands.MissingPermissions):
    await ctx.send('error: perm check failed for manage messages')

@kick.error
async def kick_error(ctx, error):
  if isinstance (error, commands.MissingPermissions):
    await ctx.send('error: you do not have permissions to kick that user')

@ban.error
async def ban_error(ctx, error):
  if isinstance (error, commands.MissingPermissions):
    await ctx.send('error: you do not have permissions to ban that user')

@unban.error
async def unban_error(ctx, error):
  if isinstance (error, commands.MissingPermissions):
    await ctx.send('error: you do not have permissions to unban that user')

bot.run('ODIxNzI3MTUzODAzNDkzNDE2.YFH7DA.wLIz7fr7Dwjo26-Dkm0dlqwbOWI')
