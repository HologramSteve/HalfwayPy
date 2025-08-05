class User:
    def __init__(self, data: dict, client):
        self.client = client
        self.username = data.get("username")
        self.public_flags = data.get("public_flags")
        self.primary_guild = data.get("primary_guild")
        self.id = data.get("id")
        self.global_name = data.get("global_name")
        self.display_name_styles = data.get("display_name_styles")
        self.discriminator = data.get("discriminator")
        self.collectibles = data.get("collectibles")
        self.clan = data.get("clan")
        self.avatar_decoration_data = data.get("avatar_decoration_data")
        self.avatar = data.get("avatar")
