from src.pages.main_page import MainPageHelper
from src.pages.login_page import LoginPageHelper


class App:
    def __init__(self, browser):
        self.browser = browser

    def main_page(self):
        return MainPageHelper(self.browser)

    def login_page(self):
        return LoginPageHelper(self.browser)
