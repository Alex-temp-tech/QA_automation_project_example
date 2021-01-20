from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun

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
    def find_element(self, locator, time=int(conftest.get_confg()['DEFAULT']['tout'])):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    @allure.step
    def find_elements(self, locator, time=int(conftest.get_confg()['DEFAULT']['tout'])):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    @allure.step
    def go_to_site(self, url):
        self.driver.get(self.base_url + url)

    @allure.step
    def go_to_site_through_token(self):
        self.driver.get(self.base_url_token)

    @allure.step
    def switch_iframe(self, locator):
        self.driver.switch_to_frame(locator)

    @allure.step
    def switch_from_iframe(self):
        self.driver.switch_to_default_content()

    @allure.step
    def screenshot(self):
        self.driver.get_screenshot_as_png()

    @allure.step
    def screenshot_for_vrt(self):
        return self.driver.get_screenshot_as_base64()

    def screenshot_check(self,vrt_name, vrt_viewport, vrt_os, vrt_device):
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
