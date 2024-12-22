# app.py
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("MVC Example")

        # Pageの初期化
        self.controllers = {
            "Page1": Page1Controller(self),
            "Page2": Page2Controller(self),
        }

        self.show_page("Page1")

    def show_page(self, page_name):
        controller = self.controllers[page_name]
        controller.show()


# base_controller.py
class BaseController:
    def __init__(self, app):
        self.app = app
        self.view = None

    def show(self):
        if self.view is None:
            self.view = self.create_view()
        self.view.pack(fill="both", expand=True)
        self.set_view_event()

    def hide(self):
        if self.view is not None:
            self.view.pack_forget()

    def create_view(self):
        raise NotImplementedError("create_view() must be implemented by subclasses.")

    def set_view_event(self):
        raise NotImplementedError("set_view_event() must be implemented by subclasses.")


# controllers.py
class Page1Controller(BaseController):
    def create_view(self):
        return Page1(self.app)

    def set_view_event(self):
        self.view.button.configure(command=lambda: self.app.show_page("Page2"))


class Page2Controller(BaseController):
    def create_view(self):
        return Page2(self.app)

    def set_view_event(self):
        self.view.button.configure(command=lambda: self.app.show_page("Page1"))


# views.py
class Page1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.build_ui()

    def build_ui(self):
        self.label = ctk.CTkLabel(self, text="Page 1")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Go to Page 2")
        self.button.pack(pady=20)


class Page2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.build_ui()

    def build_ui(self):
        self.label = ctk.CTkLabel(self, text="Page 2")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Go to Page 1")
        self.button.pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
