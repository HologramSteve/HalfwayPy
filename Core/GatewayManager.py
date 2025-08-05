import asyncio
import json
import websockets
from Types.GatewayEvent import GatewayEvent
from Types.Message import Message
import json 

class GatewayManager:
    async def handle_event(self, event: GatewayEvent) -> bool:
        print(f"event: {event.type}")
        if not event.type:
            return
        if event.type and event.type.lower() == "message_create":
            if hasattr(self, "client") and hasattr(self.client, "_event_handlers"):
                handler = self.client._event_handlers.get("handle_new_msg")
                if handler:
                    handler(Message(event.data, self.client))


    def __init__(self, token, client):
        self.token = token
        self.last_sequence = None
        self.client = client

    async def heartbeat(self, ws):
        while True:
            await ws.send(json.dumps({"op": 1, "d": self.last_sequence}))
            await asyncio.sleep(self.heartbeat_interval / 1000)

    async def connect(self):
        uri = "wss://gateway.discord.gg/?v=10&encoding=json"
        async with websockets.connect(uri) as ws:
            # receive HELLO
            msg = json.loads(await ws.recv())
            msg = GatewayEvent(msg)
            if msg.opcode != 10:
                raise ConnectionRefusedError("Expected HELLO (op 10)")
            self.heartbeat_interval = msg.data['heartbeat_interval']

            # send IDENTIFY
            identify_payload = {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": 3276799, # only server messages, will do intents later (sint juttemis)
                    "properties": {
                        "$os": "linux",
                        "$browser": "armenia",
                        "$device": "armenia"
                    }
                }
            }
            await ws.send(json.dumps(identify_payload))

            # start heartbeat
            asyncio.create_task(self.heartbeat(ws))

            # receive events
            async for raw in ws:
                payload = json.loads(raw)
                if payload.get("s") is not None:
                    self.last_sequence = payload["s"]
                await self.handle_event(GatewayEvent(payload))
