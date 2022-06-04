import json
import os
import zipfile


class Archive:

    def new_folder_name(self, id, root="media"):
        return root + "-" + str(id) + "/"

    def zipdir(self, path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(path, '..')), )

    def archive(self, type, zips, folder_name):
        print("Start compression for: ", zips)
        dst = type + "-" + str(zips) + ".zip"
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, compresslevel=3) as zipf:
            self.zipdir(folder_name, zipf)

        print("Done")

    def log_message(self, folder_name, message):
        json_message = json.dumps(message)
        path = folder_name + str(message['id']) + ".json"
        f = open(path, "x")
        f.write(json_message)
        f.close()
        print("Log message: ", message['id'])
