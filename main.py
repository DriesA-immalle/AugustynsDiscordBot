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
    await client.send_message(discord.Object(id='504650972761554984'), 'Welcome **@' + str(member) + '** to the **Augustyns Graphics Server**! :sparkles:')
    print("User Joined")

@client.event
async def on_ready():
    print("Ready to Rumble!")
client.run(TOKEN)
