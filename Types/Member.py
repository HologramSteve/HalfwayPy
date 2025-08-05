class Member:
    def __init__(self, data: dict, client):
        self.client = client
        self.roles = data.get("roles", [])
        self.premium_since = data.get("premium_since")
        self.pending = data.get("pending")
        self.nick = data.get("nick")
        self.mute = data.get("mute")
        self.joined_at = data.get("joined_at")
        self.flags = data.get("flags")
        self.deaf = data.get("deaf")
        self.communication_disabled_until = data.get("communication_disabled_until")
        self.banner = data.get("banner")
        self.avatar = data.get("avatar")