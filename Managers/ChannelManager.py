from Types.Channel import Channel

class ChannelManager:
    def __init__(self, client):
        self.requests = client.ClientRequests
        self.client = client
    
    def fetch(self, id):
        return Channel(client=self.client, data=self.requests.get(f"/channels/{id}"))