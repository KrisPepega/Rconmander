import os
import json
from .generic_rcon import rcon_emit_cmd


# TODO: Redundant?
class CommandHandler:
    def __init__(self, cmd_file: str) -> None:
        self.cmd_data = json.load(open(cmd_file))

    def parse_cmd_from(self) -> None:
        print(self.cmd_data)
