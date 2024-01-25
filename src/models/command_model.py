import json
from ..globals import DEBUG, CMD_PATH
from ..repositories.command_repo import ICommandRepository


class CommandModel(ICommandRepository):
    def __init__(self) -> None:
        self.current_game = ""
        self.cmd_file = {}

    def add_command(
        self, iid: str, ip: str, port: int, password: str, game: str
    ) -> None:
        pass

    def get_command_by_id(self, id) -> dict:
        pass

    def get_command_by_name(self, name: str) -> dict:
        return self.cmd_file["commands"][name]

    def get_commands(self):
        self.update_file()
        return self.cmd_file["commands"]

    def update_command(self, id: str, key: str, value) -> None:
        pass

    def remove_command(self, id: str) -> None:
        pass

    def update_file(self):
        self.cmd_file = json.load(open(f"{CMD_PATH}\\{self.current_game}.json"))

    def set_current_game(self, game: str):
        if game != "":
            self.current_game = game
