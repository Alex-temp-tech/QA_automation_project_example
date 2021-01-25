from selenium.webdriver.common.by import By
from src.base_page import BasePage
import allure

class MainPageLoginLokators:
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//*[@type='email']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//*[@type='password']")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//*[@type='submit']")
    LOCATOR_CHECK_CREATE_COURS = (By.LINK_TEXT, "Создать курс в папке")
    LOCATOR_CHECK_INVALID_CREDENTIALS = (By.XPATH, "//*[@role='alert']")


class LoginPageHelper(BasePage):

    @allure.step
    def enter_email(self, login):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_EMAIL_FIELD)
        search_field.send_keys(login)
        return self

    @allure.step
    def enter_password(self, pas):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_PASSWORD_FIELD)
        search_field.send_keys(pas)
        return self

    @allure.step
    def click_on_the_enter_button(self):
        return self.find_element(MainPageLoginLokators.LOCATOR_ENTER_BUTTON).click()

    @allure.step
    def full_login(self, acc):
        login = acc["login"]
        pas = acc["pass"]
        self.enter_email(login)
        self.enter_password(pas)
        self.click_on_the_enter_button()
        return self

    @allure.step
    def login_check(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_CREATE_COURS)
        assert check_el.is_displayed()
        return self

    @allure.step
    def check_invalid_credentials(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_INVALID_CREDENTIALS)
        assert check_el.is_displayed()
        return self
