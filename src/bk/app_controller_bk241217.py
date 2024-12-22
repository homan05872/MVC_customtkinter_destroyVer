import customtkinter as ctk
from typing import Any

class AppController:
    """全てのコントローラクラスを管理するクラス
    """
    def __init__(self, root:ctk.CTk) -> None:
        """ 初期化処理

        Args:
            root (ctk.CTk): CutomeTkinterインスタンス
        """
        self.root = root
        # 現在表示しているビューのコントローラ
        self.current_conn = None
        # 全てのコントローラ
        self.conns = {}
    
    def set_conns(self, controller:Any, template_name:str=None) -> None:
        """ 管理するコントローラクラスの登録処理(変数[self.conns]で管理)

        Args:
            view_class (Any): ビュークラス
            controller (Any): コントローラクラスのインスタンス
            template_name (str, optional): テンプレート名. ※Noneの場合はビュークラス名
        """
        if template_name:
            page_key = template_name
        else:    
            page_key = controller.ViewClass.__name__
        self.conns[page_key] = controller

    def show_page(self, template_name:str) -> None:
        """ ページ遷移呼び出し処理

        Args:
            template_name (str): ページ名
        """
        controller = self.conns[template_name]
        controller.show()
        