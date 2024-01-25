import tkinter as tk
from tkinter import ttk
import re
import os
from typing import List
from ..globals import DEBUG, CMD_PATH
from ..repositories.server_repo import IServerRepository


def validate_ip(ip) -> bool:
    if (
        ip == None
        or re.search("^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$", ip) == None
    ):
        return False
    return True


def validate_port(port) -> bool:
    if not (isinstance(port, int)):
        return False
    return True


class ServerModel(IServerRepository):
    def __init__(self) -> None:
        self.__servers = {}
        self.__games = []

    def add_server(
        self, iid: str, ip: str, port: int, password: str, game: str
    ) -> None:
        id = f"{ip}:{port}"
        if not (validate_ip(ip)):
            raise ValueError("Invalid IP provided!")
        elif not (validate_port(port)):
            raise ValueError("Invalid port number provided!")
        elif id in self.__servers:
            raise ValueError("Server already added!")
        self.__servers[id] = {
            "iid": iid,
            "ip": ip,
            "port": port,
            "password": password,
            "game": game,
        }
        if DEBUG:
            print(self.__servers)

    def get_server_by_id(self, id) -> dict:
        if id in self.__servers:
            return self.__servers[id]
        else:
            raise KeyError("Server not in dictionary!")

    def get_server_by_iid(self, iid) -> dict:
        for server in self.__servers:
            if iid == self.__servers[server]["iid"]:
                return self.__servers[server]
        else:
            raise KeyError("Server not in dictionary!")

    def update_server(self, id: str, key: str, value) -> None:
        self.__servers[id][key] = value
        if DEBUG:
            print(self.__servers)

    def remove_server(self, id: str) -> None:
        if id in self.__servers:
            del self.__servers[id]
            if DEBUG:
                print(f"Id: {id}, deleted!")
        else:
            raise KeyError("Server not in dictionary!")

    # TODO: Move game related data to separate model
    def update_games(self) -> None:
        self.__games = os.listdir(CMD_PATH)

    def get_games(self, extension: bool = False) -> List:
        if extension:
            return self.__games()
        return [f.split(".", 1)[0].upper() for f in self.__games]
