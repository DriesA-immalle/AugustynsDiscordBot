import discord

TOKEN = 'xxx'

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith("-ping"):
        await client.send_message(message.channel, "Jesus Christ, yes I am here!")
        print("Ping Command")

@client.event
async def on_member_join(member):
    await client.send_message(discord.Object(id='504650972761554984'), 'Welcome **' + member.mention + '** to the **Augustyns Graphics Server**! :sparkles:')
    print(str(member) + ' joined')

@client.event
async def on_member_ban(member):
    await client.send_message(discord.Object(id='504652672859635714'), '**' + str(member) + '** got **Banned** from the server!')
    print(str(member) + ' got banned')

@client.event
async def on_member_unban(server, member):
    await client.send_message(discord.Object(id='504652672859635714'), '**' + str(member) + '** got **Unbanned** from the server!')
    print(str(member) + ' got unbanned')

@client.event
async def on_ready():
    print("Ready to Rumble!")
    
client.run(TOKEN)
