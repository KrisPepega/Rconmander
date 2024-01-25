import tkinter as tk
from tkinter import ttk


class ServerView(ttk.Frame):
    def __init__(self) -> None:
        super().__init__()
        PADX = 4

        # IP LABEL & ENTRY
        self.lbl_ip = ttk.Label(self, text="RCON IP: ")
        self.lbl_ip.grid(row=1, column=0, sticky=tk.W, padx=PADX)

        self.ip_var = tk.StringVar()
        self.entry_ip = ttk.Entry(self, textvariable=self.ip_var, width=20)
        self.entry_ip.grid(row=2, column=0, padx=PADX)

        # PORT LABEL & ENTRY
        self.lbl_port = ttk.Label(self, text="RCON Port: ")
        self.lbl_port.grid(row=1, column=1, sticky=tk.W, padx=PADX)
        # TODO: Only allow numeric input
        self.port_var = tk.IntVar()
        self.entry_port = ttk.Entry(self, textvariable=self.port_var, width=10)
        self.entry_port.grid(row=2, column=1, padx=PADX)

        # RCON PASSWORD LABEL & ENTRY
        self.lbl_pwd = ttk.Label(self, text="RCON password: ")
        self.lbl_pwd.grid(row=1, column=2, sticky=tk.W, padx=PADX)

        self.pwd_var = tk.StringVar()
        self.entry_pwd = ttk.Entry(self, textvariable=self.pwd_var, width=20, show="*")
        self.entry_pwd.grid(row=2, column=2, padx=PADX)

        # GAME SELECTOR
        self.game_var = tk.StringVar()
        self.lbl_game = ttk.Label(self, text="Select game: ")
        self.lbl_game.grid(row=1, column=3, sticky=tk.W, padx=PADX)
        self.sel_game = ttk.Combobox(
            self,
            state="readonly",
            postcommand=self.sel_game_clicked,
            textvariable=self.game_var,
        )
        self.sel_game.grid(row=2, column=3, padx=PADX)

        # ADD BUTTON
        self.btn_add = ttk.Button(self, text="Add", command=self.add_btn_clicked)
        self.btn_add.grid(row=2, column=4, padx=PADX)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def add_btn_clicked(self):
        if self.controller:
            self.controller.add_server_to_table(
                self.ip_var.get(),
                self.port_var.get(),
                self.pwd_var.get(),
                self.game_var.get(),
            )

    def sel_game_clicked(self):
        if self.controller:
            self.controller.update_games()
            self.sel_game["values"] = self.controller.get_games()
