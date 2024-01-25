from rcon.source import Client
from typing import List


def rcon_emit_cmd(ip: str, port: int, passwd: str, cmd: str, args: List = []) -> str:
    with Client(ip, port, passwd=passwd) as client:
        response = client.run(cmd, *args)
    return response
