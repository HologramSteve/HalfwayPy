from Core.Client import Client
from Types.Message import Message

c = Client("YOUR_TOKEN_HERE")

@c.request
def handle_new_msg(message: Message):
    if message.content == "hi":
        message.reply("hello!")

c.login()