import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("정상구동")
    game = discord.Game("인사")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("인사"):
        await message.channel.send("하이")
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
