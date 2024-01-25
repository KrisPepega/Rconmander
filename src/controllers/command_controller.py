from ..repositories.command_repo import ICommandRepository
from ..globals import DEBUG
from .controller_base import ControllerBase
from .rcon.generic_rcon import rcon_emit_cmd


class RconController(ControllerBase):
    def __init__(self) -> None:
        super().__init__({})

    def send_rcon_cmds(self, cmd_name: str, values: list):
        _values = []
        # TODO: Handle multiple & single server selection
        try:
            iids = self.views["ServerTableView"].get_selected_servers_iid()
            for iid in iids:
                server = self.model["ServerModel"].get_server_by_iid(iid)
                command = self.model["CommandModel"].get_command_by_name(cmd_name)

                for i, v in enumerate(values):
                    if command["kwargs"][i]["type"] == "int":
                        if not v.isnumeric():
                            raise ValueError(f"Non-numeric value provided for {command["kwargs"][i]["name"]}")
                        _values.append(int(v))
                    else:
                        _values.append(v)

                if command["args"]:
                    _values.append(command["args"])

                self.views["OutputView"].show_info(
                    "Rcon command sent, awaiting response..."
                )
                response = rcon_emit_cmd(
                   server["ip"],
                   server["port"],
                   server["password"],
                   command["cmd"],
                   _values,
                )
                self.views["OutputView"].show_info(response)
            if len(iids) > 1:
                self.views["OutputView"].show_success("Commands sent!")
            else:
                self.views["OutputView"].show_success("Command sent!")
        except Exception as e:
            print(e)
            self.views["OutputView"].show_error(e)

    def get_command_list(self):
        try:
            self.model["CommandModel"].set_current_game(
                self.views["ServerTableView"].get_selected_server_info()[3]
            )
            if DEBUG:
                print(self.model["CommandModel"].get_commands().keys())
            return list(self.model["CommandModel"].get_commands().keys())
        except IndexError as ie:
            self.views["OutputView"].show_error(ie)
            return []

    def create_command_entries(self, cmd_name: str):
        try:
            self.views["CommandView"].clear_parameter_entries()
            cmd = self.model["CommandModel"].get_command_by_name(cmd_name)
            if cmd["kwargs"]:
                for kw in cmd["kwargs"]:
                    self.views["CommandView"].create_parameter_entry(
                        kw["name"].capitalize().replace("_", " ") + ": "
                    )
        except Exception as e:
            print(e)

    def add_model(self, model_name: str, model):
        try:
            if not (model_name in self.model):
                self.model[model_name] = model
            else:
                raise ValueError("Model already added!")
        except ValueError as ve:
            print(ve)
