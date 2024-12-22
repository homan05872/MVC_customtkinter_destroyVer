from core import BaseController
from views import Page1
from typing import Any
from functools import partial

class Page1Controller(BaseController):
    def __init__(self, app:Any, my_model:Any=None) -> None:
        """初期化処理

        Args:
            app (Any): Appクラスのインスタンス
            my_model (_type_, optional): MyModelクラスのインスタンス. Defaults to None.
        """
        super().__init__(app, Page1)
        self.view:Page1
        self.my_model = my_model
        
    def _set_view_event(self) -> None:
        """ ビューのUI要素へイベントメソッドを紐づける為のメソッド
        """
        self.view.button.configure(command=partial(self.goto_page, "Page2"))

    def _send_view_data(self) -> dict:
        """ 画面表示用データを渡す処理

        Returns:
            dict: 表示用データ
        """
        title = self.my_model.title
        content = self.my_model.content
        
        context = {'title': title, 'content': content}
        return context
    
    