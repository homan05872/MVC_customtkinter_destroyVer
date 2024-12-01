from typing import Any
from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self, root:Any, ViewClass:Any, template_name:str=None) -> None:
        """ 初期化処理(CustomCTkクラスで管理するコントローラ群への登録処理)
        
        Args:
            root (Any): CustomCTkクラスのインスタンス
            ViewClass (Any): 管理するビュークラス
            template_name (str, optional): 管理するビュークラスのキー。※Noneの場合はビュークラス名がキーになる.
        """
        self.root = root
        self.ViewClass = ViewClass
        self.root.set_page(self.ViewClass, self, template_name)
        self.view = None

    def show(self) -> None:
        """ ページ表示処理(このこのコントローラで管理するビューの表示処理)
        """
        if self.root.now_page != None:
            self.root.now_page.view.destroy()
        data = self._send_view_data()
        self.view = self.ViewClass(self.root, self, data ,corner_radius=0)
        self.view.grid(row=0,column=0,sticky="nsew")
        self.root.now_page = self
        
    def goto_page(self, page_name:str) -> None:
        """ ページ遷移処理
        Args:
            page_name (str): 遷移するページ名
        """
        self.root.show_page(page_name)
    
    @abstractmethod
    def _send_view_data(self) -> dict | None:
        """ ビューへ表示に必要なデータを渡す処理 ※データが必要ない場合はNoneを返す

        Returns:
            dict | None: 表示データ
        """
        return None