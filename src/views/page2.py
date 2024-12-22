import customtkinter as ctk
from functools import partial
from typing import Any

class Page2(ctk.CTkFrame):
    def __init__(self, master:Any, data:dict|None, **kwargs) -> None:
        """ 初期化処理

        Args:
            master (ctk.CTk): CustomCtkクラスのインスタンス
            data (dict | None): 表示用データ
        """
        super().__init__(master, **kwargs)
        self.data = data
        
        # Gridレイアウトの設定
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # UI生成
        self.build_ui()

    def build_ui(self) -> None:
        """ UI生成処理
        """
        # 中央にフレーム配置
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=20, pady=20)
        # ページタイトル
        self.title_label = ctk.CTkLabel(self.frame, text=self.data["title"].get())
        self.title_label.grid(row=0, column=0, padx=20, pady=10)
        # ページコンテンツ
        self.content_label = ctk.CTkLabel(self.frame, text=self.data["content"].get())
        self.content_label.grid(row=1, column=0, padx=20, pady=10)
        # ページ１リンクボタン
        self.back_button = ctk.CTkButton(self.frame, text="Back to Page 1")
        self.back_button.grid(row=2, column=0, padx=20, pady=20)
