from typing import List
from ..globals import DEBUG, NA
from ..repositories.server_repo import IServerRepository
from .controller_base import ControllerBase


class ServerController(ControllerBase):
    def __init__(self, model: IServerRepository) -> None:
        super().__init__(model)

    def add_server_to_table(self, ip: str, port: int, password: str, game: str) -> None:
        try:
            self.model.add_server("", ip, port, password, game)
            iid = self.views["ServerTableView"].insert_server((NA, ip, port, game, NA))
            self.model.update_server(f"{ip}:{port}", "iid", iid)
            self.views["OutputView"].show_success("Server added!")
        except ValueError as ve:
            self.views["OutputView"].show_error(ve)
            if DEBUG:
                print(ve)

    def del_server_from_table(self, ip, port):
        try:
            self.model.remove_server(f"{ip}:{port}")
            self.views["OutputView"].show_success("Server removed!")
        except KeyError as ke:
            self.views["OutputView"].show_error(ke)
            if DEBUG:
                print(ke)

    def update_games(self) -> None:
        self.model.update_games()

    def get_games(self) -> List:
        return self.model.get_games()
