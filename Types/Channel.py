from Enums.ChannelType import ChannelType
from Managers.MessageManager import MessageManager

class Channel:
    def __init__(self, data, client):
        self.client = client
        self.id = data.get("id")
        self.messages = MessageManager(client=client, channel_id=self.id)
        # Convert type to ChannelType enum if possible
        type_value = data.get("type")
        try:
            self.type = ChannelType(type_value)
        except (ValueError, TypeError):
            self.type = type_value
        self.guild_id = data.get("guild_id")
        self.position = data.get("position")
        self.permission_overwrites = data.get("permission_overwrites", [])
        self.name = data.get("name")
        self.topic = data.get("topic")
        self.nsfw = data.get("nsfw")
        self.last_message_id = data.get("last_message_id")
        self.bitrate = data.get("bitrate")
        self.user_limit = data.get("user_limit")
        self.rate_limit_per_user = data.get("rate_limit_per_user")
        self.recipients = data.get("recipients", [])
        self.icon = data.get("icon")
        self.owner_id = data.get("owner_id")
        self.application_id = data.get("application_id")
        self.managed = data.get("managed")
        self.parent_id = data.get("parent_id")
        self.last_pin_timestamp = data.get("last_pin_timestamp")
        self.rtc_region = data.get("rtc_region")
        self.video_quality_mode = data.get("video_quality_mode")
        self.message_count = data.get("message_count")
        self.member_count = data.get("member_count")
        self.thread_metadata = data.get("thread_metadata")
        self.member = data.get("member")
        self.default_auto_archive_duration = data.get("default_auto_archive_duration")
        self.permissions = data.get("permissions")
        self.flags = data.get("flags")
        self.total_message_sent = data.get("total_message_sent")
        self.available_tags = data.get("available_tags", [])
        self.applied_tags = data.get("applied_tags", [])
        self.default_reaction_emoji = data.get("default_reaction_emoji")
        self.default_thread_rate_limit_per_user = data.get("default_thread_rate_limit_per_user")
        self.default_sort_order = data.get("default_sort_order")
        self.default_forum_layout = data.get("default_forum_layout")