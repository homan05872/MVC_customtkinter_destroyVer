import customtkinter as ctk
from typing import Any

class Page1(ctk.CTkFrame):
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
        self.label = ctk.CTkLabel(self.frame, text="This is Page 1")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        # ページ２に表示するタイトル入力
        self.title_input = ctk.CTkEntry(self.frame, textvariable=self.data["title"], width=300)
        self.title_input.grid(row=1, column=0, padx=20, pady=20)
        # ページ２に表示するコンテンツ入力
        self.content_input = ctk.CTkEntry(self.frame, textvariable=self.data["content"], width=300)
        self.content_input.grid(row=2, column=0, padx=20, pady=20)
        # ページ２リンクボタン
        self.button = ctk.CTkButton(self.frame, text="Send")
        self.button.grid(row=3, column=0, padx=20, pady=20)