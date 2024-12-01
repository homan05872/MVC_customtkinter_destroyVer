import customtkinter as ctk
from tkinterdnd2 import TkinterDnD
from typing import Any


class CustomCTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs) -> None:
        """ 初期化処理
        """
        super().__init__(*args, **kwargs)
        self.now_page:Any = None            # 現在ページのコントローラインスタンス
        self.pages_conn:dict[str,Any] = {}  # 全ページのコントローラの辞書リスト
        # テーマ設定
        ctk.set_appearance_mode('dark')       # Modes: system (default), light, dark
        ctk.set_default_color_theme('blue')   # Themes: blue (default), dark-blue, green
        
        # Gridレイアウトの設定
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.title("MVCテンプレート")   # ウィンドウキャプション
        self.geometry("550x550")       # ウィンドウサイズ
        
        # TkinterDnDのイベントを使用できるようにする設定
        self.TkdndVersion = TkinterDnD._require(self)
        
    def set_page(self, view_class:Any, controller:Any, template_name:str=None) -> None:
        """ 管理するコントローラクラスの登録処理(変数[self.pages_conn]で管理)

        Args:
            view_class (Any): ビュークラス
            controller (Any): コントローラクラスのインスタンス
            template_name (str, optional): テンプレート名. ※Noneの場合はビュークラス名
        """
        if template_name:
            page_name = template_name
        else:    
            page_name = view_class.__name__
        self.pages_conn[page_name] = controller

    def show_page(self, page_name:str) -> None:
        """ ページ遷移呼び出し処理

        Args:
            page_name (str): ページ名
        """
        controller = self.pages_conn[page_name]
        controller.show()