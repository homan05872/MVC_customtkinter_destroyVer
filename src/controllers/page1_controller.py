from core import BaseController
from views import Page1
from typing import Any

class Page1Controller(BaseController):
    def __init__(self, root:Any, my_model=None) -> None:
        """初期化処理

        Args:
            root (Any): CustomCtkクラスのインスタンス
            my_model (_type_, optional): MyModelクラスのインスタンス. Defaults to None.
        """
        super().__init__(root, Page1)
        self.my_model = my_model

    def _send_view_data(self) -> dict:
        """ 画面表示用データを渡す処理

        Returns:
            dict: 表示用データ
        """
        title = self.my_model.title
        content = self.my_model.content
        
        context = {'title': title, 'content': content}
        return context
