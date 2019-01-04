import time
import os
from WebWhatsApi import WhatsAPIDriver
from WebWhatsApi.objects.message import Message, MediaMessage, MMSMessage

path = './WebWhatsApi/chrome-cache/'
path = os.path.abspath(path)
print(path)
options = ['--profile-directory=Default', '--user-data-dir=' + path]
driver = WhatsAPIDriver(client='chrome', profile=path, chrome_options=options)

# driver.get_qr()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

# for c in driver.get_contacts():
#     print(c.name + ": " + c.id)

while True:
    time.sleep(3)
    for contact in driver.get_unread():
        for message in contact.messages:

            if message.sender.id == "Sender Chat ID":

                if isinstance(message, MMSMessage):
                    message.save_media('', True)
                    contact.chat.send_media(message.filename)  # message.client_url
                    contact.chat.send_message("Sorry, i'm kind of deaf...")
                elif isinstance(message, MediaMessage):
                    message.save_media('', True)
                    contact.chat.send_media(message.filename)  # message.client_url
                    contact.chat.send_message("That's a great media!")
                elif isinstance(message, Message):
                    if 'oi' in message.content.lower():
                        contact.chat.send_message("Hey there")
                    else:
                        contact.chat.send_message(message.content)
                    print(message)
                else:
                    print("Message type not supported")
            else:
                print(contact.chat.id)
