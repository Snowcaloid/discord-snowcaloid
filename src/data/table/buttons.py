from data.table.definition import TableDefinition, ColumnType, ColumnFlag, ColumnDefinition
from typing import List

class ButtonData:
    button_id: str
    label: str
    
    def __init__(self, button_id: str, label: str = ''):
        self.button_id = button_id
        self.label = label
    
class ButtonsTable(TableDefinition):
    _columns: List[ColumnDefinition] = []
    def init_definitions(self):
        self.define_field('button_id', ColumnType.VARCHAR, 50, [ColumnFlag.UNIQUE, ColumnFlag.PRIMARY_KEY])
        self.define_field('label', ColumnType.VARCHAR, 50)