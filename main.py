import asyncio
import io
import discord
from PIL import Image, ImageDraw, ImageFont, ImageSequence


DISCORD_BOT_TOKEN = "your token"
SERVER_ID = none #your id 


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def create_banner(members_count: int):
    img = Image.open("tst.gif")
    frames = []
    for frame in ImageSequence.Iterator(img):
        
        d = ImageDraw.Draw(frame)
        font = ImageFont.truetype("2.ttf", 71)
        d.text((img.width - 258, 399), str(members_count), font=font, fill=(255, 255, 255))
        del d

        b = io.BytesIO()
        frame.save(b, format="GIF", )
        frame = Image.open(b)

        frames.append(frame)
    frames[0].save('updated_banner.gif', save_all=True, append_images=frames[1:])


@client.event
async def on_ready():
    while True:
        server = client.get_guild(SERVER_ID)
        members_in_voice = 0
        for member in server.members:
            if member.voice:
                members_in_voice += 1
        create_banner(members_count=members_in_voice)
        await server.edit(banner=open("updated_banner.gif", "rb").read())
        print("Banner changed")
        await asyncio.sleep(5)




if __name__ == '__main__':
    client.run(DISCORD_BOT_TOKEN)
