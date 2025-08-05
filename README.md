# HalfwayPi

HalfwayPi is a minimal, modular Python library for working with the Discord API. It aims to be easy to read, easy to extend, and not too fancy.

# Important: you can't do shit with this, do not use!

## Features
- Simple HTTP and WebSocket (gateway) support
- Clean separation of client, managers, and data types
- Event handler system using decorators
- Type-safe enums for Discord types
- No unnecessary dependencies

## Quick Example

```python
from Core.Client import Client
from Types.Message import Message

c = Client("YOUR_TOKEN_HERE")

@c.request
def handle_new_msg(message: Message):
    if message.content == "hi":
        message.reply("hello!")

c.login()
```

## Project Structure

- `Core/` - Main client, gateway, and HTTP logic
- `Types/` - Data models (Message, Channel, User, etc.)
- `Managers/` - Resource managers (ChannelManager, MessageManager)
- `Enums/` - Enum types for Discord constants

## Requirements
- Python 3.8+
- `requests` and `websockets` libraries

## Notes
- You need to enable the right intents for your bot in the Discord Developer Portal to receive message content and other privileged events.
- This project is for learning, hacking, and small bots. For big bots, check out discord.py or nextcord.

## License
MIT
