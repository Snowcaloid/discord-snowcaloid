from data.table.definition import TableDefinition, ColumnType, ColumnFlag
from data.table.schedule import ScheduleType

class ChannelData:
    guild_id: int
    type: ScheduleType
    channel_id: int
    is_pl_channel: bool
    is_support_channel: bool
    
    def __init__(self, guild_id: int, type: ScheduleType, channel_id: int, is_pl_channel: bool = False, is_support_channel: bool = False):
        self.guild_id = guild_id
        self.type = type
        self.channel_id = channel_id
        self.is_pl_channel = is_pl_channel
        self.is_support_channel = is_support_channel
    
class ChannelTable(TableDefinition):
    def init_definitions(self):
        self.define_column('id', ColumnType.SERIAL, 0, [ColumnFlag.UNIQUE])
        self.define_column('guild_id', ColumnType.BIGINT)
        self.define_column('type', ColumnType.VARCHAR, 15)
        self.define_column('channel_id', ColumnType.BIGINT)
        self.define_column('is_pl_channel', ColumnType.BOOLEAN)
        self.define_column('is_support_channel', ColumnType.BOOLEAN)