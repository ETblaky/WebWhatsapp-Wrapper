import time
import os
from WebWhatsApi import WhatsAPIDriver
from WebWhatsApi.objects.message import Message

path = './WebWhatsApi/chrome-cache/'
path = os.path.abspath(path)
print(path)
options = ['--profile-directory=Default', '--user-data-dir=' + path]
driver = WhatsAPIDriver(client='chrome', profile=path, chrome_options=options)

print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):
                # contact.chat.send_message(message.content)
                print(message)
