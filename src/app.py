import tkinter as tk
from tkinter import ttk

from src.views.server_view import ServerView
from src.views.server_table_view import ServerTableView
from src.views.output_view import OutputView
from src.views.command_view import CommandView

from src.models.server_model import ServerModel
from src.models.command_model import CommandModel

from src.controllers.server_controller import ServerController
from src.controllers.command_controller import RconController


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        PADX = (10, 10)
        PADY = (5, 5)

        # START_WIDTH = 1280
        # START_HEIGTH = 720
        MIN_WIDTH = 100
        MIN_HEIGTH = 100

        self.title("RCONMANDER")
        # self.geometry = f"{START_WIDTH}x{START_HEIGTH}"
        self.minsize = f"{MIN_WIDTH}x{MIN_HEIGTH}"

        server_model = ServerModel()
        command_model = CommandModel()

        server_view = ServerView()
        server_view.grid(row=0, column=0, padx=PADX, pady=PADY, sticky=tk.W)

        server_table_view = ServerTableView()
        server_table_view.grid(row=1, column=0, padx=PADX, pady=PADY, sticky=tk.W)

        output_view = OutputView()
        output_view.grid(row=2, column=0, padx=PADX, pady=PADY, sticky=tk.W)

        command_view = CommandView()
        command_view.grid(row=1, column=1, padx=PADX, pady=PADY, sticky=tk.NW)

        server_controller = ServerController(server_model)
        server_controller.add_view("ServerView", server_view)
        server_controller.add_view("ServerTableView", server_table_view)
        server_controller.add_view("OutputView", output_view)

        output_view.set_controller(server_controller)
        server_view.set_controller(server_controller)
        server_table_view.set_controller(server_controller)

        rcon_controller = RconController()
        rcon_controller.add_model("ServerModel", server_model)
        rcon_controller.add_model("CommandModel", command_model)

        rcon_controller.add_view("ServerTableView", server_table_view)
        rcon_controller.add_view("OutputView", output_view)
        rcon_controller.add_view("CommandView", command_view)

        command_view.set_controller(rcon_controller)
