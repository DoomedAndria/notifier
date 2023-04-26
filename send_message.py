from discord import Webhook
import aiohttp
import asyncio

WEBHOOK = 'https://discord.com/api/webhooks/1100734930763399198/boK6KdEcveIuizIliuSXCrrgg1YUPNNdCi3dp_EPon3NI8kM67dQxnE16vp9P_xRwPc-'
username = 'Bizina ivanishvili'
avatar_url = 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Bidzina_Ivanishvili_2013-07-19.jpg'


def send_message(msg):
    async def message(msg1):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(WEBHOOK, session=session)
            await webhook.send(msg1, username=username,
                               avatar_url=avatar_url)

    asyncio.run(message(msg))



def send_sachkhere(dates):
    message_sachkhere = 'საჩხერე:\n\n'
    if len(dates) == 0:
        message_sachkhere += "საგამოცდო თარიღი ვერ მოიძებნა"
    else:
        for i in dates:
            message_sachkhere += i + "\n"
    send_message(message_sachkhere)
