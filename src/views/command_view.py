import tkinter as tk
from tkinter import ttk
from typing import Any


class CommandEntry(ttk.Frame):
    def __init__(self, parent, label: str) -> None:
        super().__init__(parent)
        PADX = 0
        PADY = 2

        self.lbl = ttk.Label(self, text=label)
        self.lbl.grid(row=0, padx=PADX, pady=PADY, sticky=tk.W)

        self.input_value = tk.StringVar()
        self.user_input = ttk.Entry(self, textvariable=self.input_value, width=30)
        self.user_input.grid(row=1, padx=PADX, pady=PADY)

    def get_value(self):
        return self.input_value.get()


class CommandView(ttk.Frame):
    def __init__(self) -> None:
        super().__init__()
        PADX = 0
        PADY = 4
        self.param_entries = []
        self.controller = None

        self.lbl_cmd = ttk.Label(self, text="Command: ")
        self.lbl_cmd.pack(side=tk.TOP, anchor=tk.W, padx=PADX)

        self.cmd_var = tk.StringVar()
        self.sel_cmd = ttk.Combobox(
            self,
            state="readonly",
            postcommand=self.sel_cmd_clicked,
            textvariable=self.cmd_var,
        )
        self.sel_cmd.pack(side=tk.TOP, anchor=tk.W, padx=PADX)
        self.sel_cmd.bind("<<ComboboxSelected>>", self.cmd_selected)

        self.btn_cmd_send = ttk.Button(
            self, text="Send", command=self.send_cmds, state=tk.DISABLED
        )
        self.btn_cmd_send.pack(side=tk.TOP, anchor=tk.W, padx=PADX, pady=PADY)

    def sel_cmd_clicked(self):
        if self.controller:
            values = self.controller.get_command_list()
            if len(values) == 0:
                self.sel_cmd.set("")
            self.sel_cmd["values"] = values

    def cmd_selected(self, event):
        self.controller.create_command_entries(self.cmd_var.get())
        self.btn_cmd_send["state"] = tk.ACTIVE

    def set_controller(self, controller):
        self.controller = controller

    def create_parameter_entry(self, label):
        param_entry = CommandEntry(self, label)
        param_entry.pack(side=tk.TOP, anchor=tk.W)
        self.param_entries.append(param_entry)

    def clear_parameter_entries(self):
        while len(self.param_entries) != 0:
            self.param_entries.pop().destroy()

    def send_cmds(self):
        values = []
        for e in self.param_entries:
            values.append(e.get_value())
        self.controller.send_rcon_cmds(self.cmd_var.get(), values)
