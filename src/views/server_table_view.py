import tkinter as tk
from tkinter import ttk
from typing import Tuple


class ServerTableView(ttk.Frame):
    def __init__(self) -> None:
        super().__init__()
        SERVER_COLUMNS = ("Hostname", "IP", "Port", "Game", "Players")
        PADX = 10
        PADY = 2
        HEIGHT = 10
        self.controller = None

        self.lbl_servers = ttk.Label(self, text="Servers: ")
        self.lbl_servers.grid(row=0, column=0, sticky=tk.W)

        self.server_tree = ttk.Treeview(
            self, columns=SERVER_COLUMNS, show="headings", height=HEIGHT
        )
        self.server_tree.grid(row=1, column=0)
        for c in SERVER_COLUMNS:
            self.server_tree.heading(c, text=c)
            if c == "Players" or c == "Game":
                self.server_tree.column(c, width=50)
            else:
                self.server_tree.column(c, width=175)

        # RIGHT-CLICK MENU FOR SERVERS
        # TODO: Add extended functionality
        self.menu = tk.Menu(self.server_tree, tearoff=0)
        self.menu.add_command(label="delete", command=self.remove_selected_servers)
        # self.menu.add_command(label="reload")
        # self.menu.add_command(label="info")
        self.menu.add_separator()
        self.menu.add_command(label="close")

        self.server_tree.bind("<Button-3>", self.do_popup)

    def do_popup(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def insert_server(self, server_info: Tuple) -> str:
        item = self.server_tree.insert("", tk.END, values=server_info)
        return item

    def update_server(self, iid):
        pass

    def get_selected_server_info(self):
        try:
            selected_iid = self.server_tree.selection()[0]
            return self.server_tree.item(selected_iid)["values"]
        except IndexError:
            raise IndexError("No server selected in table!")

    def get_selected_servers_iid(self):
        return self.server_tree.selection()

    def remove_selected_servers(self):
        selected_iids = self.server_tree.selection()
        for iid in selected_iids:
            server = self.server_tree.item(iid)
            self.controller.del_server_from_table(
                server["values"][1], server["values"][2]
            )
            self.server_tree.delete(iid)

    # TODO: Implement server sub items i.e. full player list
    # def insert_server_item(self):
    #    pass

    # def update_server_item(self):
    #    pass

    # def remove_server_item(self):
    #    pass

    def set_controller(self, controller):
        self.controller = controller
