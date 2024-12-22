from typing import Any
from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self, app:Any, ViewClass:Any) -> None:
        """ 初期化処理(CustomCTkクラスで管理するコントローラ群への登録処理)
        
        Args:
            app (Any): Appインスタンス
            ViewClass (Any): 管理するビュークラス
        """
        self.app = app 
        self.root = app.root
        self.ViewClass = ViewClass
        self.view = None

    def show(self) -> None:
        """ ページ表示処理(このコントローラで管理するビューの表示処理)
        """
        # ビューデータの取得
        data = self._send_view_data()
        # 現在ビュー表示の削除
        if self.app.current_conn != None:
            self.app.current_conn.view.destroy()
        # 次のビュー表示
        self.view = self.ViewClass(self.root, data ,corner_radius=0)
        self.view.grid(row=0,column=0,sticky="nsew")
        # 次のビューのコントローラをAppで保持
        self.app.current_conn = self
        # ビューUI要素に紐づけるイベントメソッドを設定する
        self._set_view_event()
        
    def goto_page(self, template_name:str) -> None:
        """ ページ遷移処理
        Args:
            template_name (str): 遷移するページ名
        """
        self.app.show_page(template_name)
    
    @abstractmethod
    def _set_view_event(self) -> None:
        """ ビューのUI要素へイベントメソッドを紐づける為のメソッド
        """
        pass
    
    @abstractmethod
    def _send_view_data(self) -> dict | None:
        """ ビューへ表示に必要なデータを渡す処理 ※データが必要ない場合はNoneを返す

        Returns:
            dict | None: 表示データ
        """
        return None