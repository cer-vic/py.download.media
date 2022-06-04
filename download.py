import os
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterUrl

from archive import Archive


def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))


class Download:

    def __init__(self, client, group_name, delete):
        self.zips = 1
        self.items = 0
        self.group_name = group_name
        self.client = client
        self.archive = Archive()
        self.delete = delete

    def links(self):
        for message in self.client.iter_messages(self.group_name, filter=InputMessagesFilterUrl):
            folder_name = self.archive.new_folder_name(self.zips, "links")
            os.mkdir(folder_name)
            # print(message.id, message)
            self.items += 1
            log = {
                'id': message.id,
                'message': message.message,
                'date': str(message.date),
            }
            self.archive.log_message(folder_name, log)

            if self.items == 20:
                self.archive.archive("links", self.zips, folder_name)
                self.zips += 1
                self.items = 0
                exit()

    def media(self):
        for message in self.client.iter_messages(self.group_name, filter=InputMessagesFilterPhotos):
            folder_name = self.archive.new_folder_name(id=self.zips)

            if message.media:
                file = self.client.download_media(message, file=folder_name,
                                                  progress_callback=callback)
                log = {
                    'id': message.id,
                    'raw_text': message.raw_text,
                    'peer_id': message.peer_id.user_id,
                    'date': str(message.date),
                    'mentioned': message.mentioned,
                    'post': message.post,
                    'fwd_from': message.fwd_from,
                    'reply_to': message.reply_to,
                    "file": file
                }
                self.archive.log_message(folder_name, log)
                self.items += 1

                if self.items == 20:
                    self.archive.archive("media", self.zips, folder_name)
                    self.zips += 1
                    self.items = 0
                    exit()
