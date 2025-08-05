from .ClientRequests import ClientRequests
from .GatewayManager import GatewayManager
from Managers.ChannelManager import ChannelManager


class Client:
    def __init__(self, token):
        self.token = token
        self.ClientRequests = ClientRequests(self.token)
        self.channels = ChannelManager(self)
        self.GatewayManager = GatewayManager(self.token, self)
        self._event_handlers = {}

        
    
    def login(self):
        import asyncio
        asyncio.run(self.GatewayManager.connect())


    def request(self, func):
        event_name = func.__name__
        self._event_handlers[event_name] = func
        return func