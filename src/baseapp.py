from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from src import save_token
from tests import conftest
import allure


class BasePage:
    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://antitreningi.ru"
        self.base_url_token = "https://antitreningi.ru/account/auth?&token=" + save_token.token()

    @allure.step
    def find_element(self, locator, time=conftest.T_OUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    @allure.step
    def find_elements(self, locator, time=conftest.T_OUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    #go to page
    @allure.step
    def go_to_site(self, url):
        self.driver.get(self.base_url + url)

    @allure.step
    def go_to_site_through_token(self):
        self.driver.get(self.base_url_token)

    @allure.step
    def switch_iframe(self, locator):
        time.sleep(3)
        self.driver.switch_to_frame(locator)

    @allure.step
    def switch_from_iframe(self):
        self.driver.switch_to_default_content()

    @allure.step
    def screenshot(self):
        self.driver.get_screenshot_as_png()

    def screenshot_for_vrt(self):
        return self.driver.get_screenshot_as_base64()
