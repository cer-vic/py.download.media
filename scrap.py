from telethon import TelegramClient, sync
import os
# import logging
# import asyncio
# import socks

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
group_name = os.environ.get("GROUP_NAME")
# logging.basicConfig(level=logging.DEBUG)
client = TelegramClient('test2', api_id, api_hash)


client.start()


def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))


for message in client.iter_messages(group_name):
    if message.media:
        client.download_media(message, progress_callback=callback)


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
