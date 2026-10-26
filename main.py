import os
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot đã online thành công: {client.user}')

@client.event
async def on_member_join(member):
    member_count = member.guild.member_count
    for channel in member.guild.text_channels:
        if channel.name == "welcome":
            await channel.send(f"WELCOME TO MY SERVER!!! {member.mention}! Member #{member_count}")
            break

# Lấy token từ biến môi trường trên Render để bảo mật tuyệt đối
client.run(os.environ['MTU2NDI3MzIzOTYyMTExNjA0Ng.GP6RR9.QLrZ83vEspHuGVnsQ9QN27mE8LfevZp8zYo2vY'])
