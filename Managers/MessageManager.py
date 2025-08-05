from Types.Message import Message

class MessageManager:
    def __init__(self, client, channel_id):
        self.channel_id = channel_id
        self.requests = client.ClientRequests
        self.client = client
    
    def fetch(self, id):
        return Message(client=self.client, data=self.requests.get(f"/channels/{self.channel_id}/messages/{id}"))