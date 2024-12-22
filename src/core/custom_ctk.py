import customtkinter as ctk
from tkinterdnd2 import TkinterDnD


class CustomCTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs) -> None:
        """ CustomTkinter全体の設定
        """
        super().__init__(*args, **kwargs)
        
        # テーマ設定
        ctk.set_appearance_mode('dark')       # Modes: system (default), light, dark
        ctk.set_default_color_theme('blue')   # Themes: blue (default), dark-blue, green
        
        # Gridレイアウトの設定（ビューを画面いっぱいに表示するため）
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.title("MVCテンプレート")   # ウィンドウキャプション
        self.geometry("550x550")       # ウィンドウサイズ
        
        # TkinterDnDのイベントを使用できるようにする設定
        self.TkdndVersion = TkinterDnD._require(self)