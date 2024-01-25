import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk


class OutputView(ttk.Frame):
    def __init__(self) -> None:
        super().__init__()
        PADX = 10
        PADY = 2

        WIDTH = 75
        HEIGHT = 10

        self.controller = None

        self.lbl_output = tk.Label(self, text="Output: ")
        self.lbl_output.grid(row=0, column=0, sticky=tk.W)

        self.txt_output = st.ScrolledText(self, width=WIDTH, height=HEIGHT)
        self.txt_output.grid(row=1, column=0)
        self.txt_output.config(state="disabled")

    def show_msg(self, prefix: str, msg: str):
        self.txt_output.configure(state="normal")
        self.txt_output.insert(tk.END, f"{prefix} {msg}\n")
        self.txt_output.configure(state="disabled")

    def show_info(self, msg: str):
        info_prefix = "INFO:"
        self.show_msg(info_prefix, msg)

    def show_success(self, msg: str):
        success_prefix = "SUCCESS:"
        self.show_msg(success_prefix, msg)

    def show_error(self, msg: str):
        error_prefix = "ERROR:"
        self.show_msg(error_prefix, msg)

    def set_controller(self, controller):
        self.controller = controller
