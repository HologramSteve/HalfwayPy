
from Enums.MessageType import MessageType
from Types.Member import Member
from Types.User import User

class Message:
    def __init__(self, data, client):
        type_value = data.get('type')
        try:
            self.type = MessageType(type_value)
        except (ValueError, TypeError):
            self.type = type_value
        self.content = data.get('content')
        self.mentions = data.get('mentions', [])
        self.mention_roles = data.get('mention_roles', [])
        self.attachments = data.get('attachments', [])
        self.embeds = data.get('embeds', [])
        self.timestamp = data.get('timestamp')
        self.edited_timestamp = data.get('edited_timestamp')
        self.flags = data.get('flags')
        self.components = data.get('components', [])
        self.id = data.get('id')
        self.channel_id = data.get('channel_id')
        self.pinned = data.get('pinned', False)
        self.mention_everyone = data.get('mention_everyone', False)
        self.tts = data.get('tts', False)
        self.client = client

        # Parse member and author (user)
        self.member = Member(data.get('member', {}), client) if data.get('member') else None
        self.user = User(data.get('author', {}), client) if data.get('author') else None
    
    def delete(self):
        self.client.ClientRequests.delete(f"/channels/{self.channel_id}/messages/{self.id}")
        return True

    def edit(self, content=None, embeds=None, flags=None, components=None):
        payload = {}
        if content is not None:
            payload['content'] = content
        if embeds is not None:
            payload['embeds'] = embeds
        if flags is not None:
            payload['flags'] = flags
        if components is not None:
            payload['components'] = components

        self.client.ClientRequests.patch(
            f"/channels/{self.channel_id}/messages/{self.id}",
            data=payload
        )
        return True
    def reply(self, content, allowed_mentions=None, embeds=None, components=None):
        payload = {
            "content": content,
            "message_reference": {
                "message_id": self.id,
                "channel_id": self.channel_id
            }
        }
        if allowed_mentions is not None:
            payload["allowed_mentions"] = allowed_mentions
        if embeds is not None:
            payload["embeds"] = embeds
        if components is not None:
            payload["components"] = components

        self.client.ClientRequests.post(
            f"/channels/{self.channel_id}/messages",
            data=payload
        )
        return True