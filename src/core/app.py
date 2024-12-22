from controllers import Page1Controller, Page2Controller
from models.mymodel import MyModel
from core.custom_ctk import CustomCTk

class App:
    """全てのコントローラクラスを管理するクラス
    """
    def __init__(self) -> None:
        """ 初期化処理
        """
        
        self.root = CustomCTk()
        # モデルの初期化
        self.my_model = MyModel()
        # コントローラの初期化(全てのコントローラはself.connsで管理)
        self.conns = {
            'Page1':Page1Controller(self, self.my_model),
            'Page2':Page2Controller(self, self.my_model)
        }
        # 現在表示しているビューのコントローラ
        self.current_conn = None

    def show_page(self, template_name:str) -> None:
        """ ページ遷移呼び出し処理

        Args:
            template_name (str): ページ名
        """
        controller = self.conns[template_name]
        controller.show()
        
    def run(self) -> None:
        """ アプリ起動
        """
        # 最初のページを表示
        self.show_page('Page1')
        # メインループ
        self.root.mainloop()