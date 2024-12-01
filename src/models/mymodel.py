import tkinter as tk

class MyModel:
    def __init__(self) -> None:
        self.title = tk.StringVar(value="Page 2 Title")
        self.content = tk.StringVar(value="This is the content of Page 2")