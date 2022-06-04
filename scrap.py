from telethon import TelegramClient
import os

from download import Download
# import logging
# import asyncio
# import socks

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
group_name = os.environ.get("GROUP_NAME")
# logging.basicConfig(level=logging.DEBUG)
client = TelegramClient('test2', api_id, api_hash)


client.start()
downloader = Download(client, group_name, False)
downloader.links()

# def load_messages():
#     dialogs = client.get_dialogs()
#     chat = None

#     for dialog in dialogs:
#         print(dialog)
#         if dialog.name == "group_name":
#             chat = dialog
#             break

#     for message in client.iter_messages(chat):
#         if message.media:
#             print('Downloading...')
#             client.download_media(message)

# load_messages()
