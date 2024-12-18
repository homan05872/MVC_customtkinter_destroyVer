from models.mymodel import MyModel
from core import CustomCTk
from controllers import Page1Controller, Page2Controller
from models.mymodel import MyModel

class App:
    def __init__(self) -> None:
        """ 初期化処理
        """
        self.root = CustomCTk()
        
        # モデルの初期化
        self.my_model = MyModel()
        
        # コントローラの初期化
        self.page1_conn = Page1Controller(self.root, self.my_model)
        self.page2_conn = Page2Controller(self.root, self.my_model)

    def run(self) -> None:
        """ アプリ起動
        """
        # 最初のページを表示
        self.page1_conn.show()
        # メインループ
        self.root.mainloop()