from models.mymodel import MyModel
from core import CustomCTk
from controllers import Page1Controller, Page2Controller
from models.mymodel import MyModel
from core.app import App

class App:
    def __init__(self) -> None:
        """ 初期化処理
        """
        self.root = CustomCTk()
        
        # モデルの初期化
        self.my_model = MyModel()
        
        # コントローラの初期化
        self.page1_conn = Page1Controller(self.app_conn, self.my_model, template_name='Page1')
        self.page2_conn = Page2Controller(self.app_conn, self.my_model, template_name='Page2')

    def run(self) -> None:
        """ アプリ起動
        """
        # 最初のページを表示
        self.app_conn.show_page('Page1')
        # メインループ
        self.root.mainloop()