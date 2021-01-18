from selenium.webdriver.common.by import By
from src.baseapp import BasePage
import allure
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun
import time


class MainPageLoginLokators:
    LOCATOR_BUTTON_LOGIN = (By.XPATH, "//span[contains(text(),'Войти')]")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@name='login']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOCATOR_ENTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOCATOR_CHECK_CREATE_COURS = (By.LINK_TEXT, "Создать курс в папке")
    LOCATOR_CHECK_INVALID_CREDENTIALS = (By.XPATH, "//*[@class='responseError']")


class MainPageHelper(BasePage):

    @allure.step
    def click_on_the_yellow_button(self):
        self.find_element(MainPageLoginLokators.LOCATOR_BUTTON_LOGIN).click()

    @allure.step
    def enter_email(self, login):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_EMAIL_FIELD)
        search_field.send_keys(login)

    @allure.step
    def enter_password(self, pas):
        search_field = self.find_element(MainPageLoginLokators.LOCATOR_PASSWORD_FIELD)
        search_field.send_keys(pas)

    @allure.step
    def click_on_the_enter_button(self):
        self.find_element(MainPageLoginLokators.LOCATOR_ENTER_BUTTON).click()

    @allure.step
    def full_login(self, acc):
        login = acc["login"]
        pas = acc["pass"]
        self.click_on_the_yellow_button()
        self.enter_email(login)
        self.enter_password(pas)
        self.click_on_the_enter_button()

    @allure.step
    def login_check(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_CREATE_COURS)
        assert check_el.is_displayed()

    @allure.step
    def check_invalid_credentials(self):
        check_el = self.find_element(MainPageLoginLokators.LOCATOR_CHECK_INVALID_CREDENTIALS)
        assert check_el.is_displayed()


    def screenshot_check(self, vrt_name, vrt_viewport, vrt_os, vrt_device):
        config = Config(
            # apiUrl - URL where backend is running
            apiUrl='http://104.248.78.141:4200',

            # project - Project name or ID
            project='at-test',

            # apiKey - User apiKey
            apiKey='YYJSBHYHD0MB77PFBNBFJ6X79FRZ',

            # ciBuildId - Current git commit SHA
            ciBuildId='prod',

            # branch - Current git branch
            branchName='at-test',

            # enableSoftAssert - Log errors instead of exceptions
            enableSoftAssert=False,
        )

        vrt = VisualRegressionTracker(config)
        scr = self.screenshot_for_vrt()
        with vrt:
            vrt.track(TestRun(
                name=vrt_name,
                imageBase64=scr,
                diffTollerancePercent=0,
                os=vrt_os,
                browser='Chrome',
                viewport=vrt_viewport,
                device=vrt_device,
            ))
