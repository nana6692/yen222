import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("인사")
    await client.change_presence(status=discord.Status.online, activity=game)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)




client.run("d7f0ea40723365a33d83867054803febbdf8c8d2c7450f60e93f2f6ed9289fce")