from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun
from configuration import Configuration
from src import save_token
import allure


class BasePage:
    def __init__(self, browser):
        self.driver = browser
        self.base_url = Configuration.base_url
        self.base_url_token = Configuration.base_url + save_token.token()

    @allure.step
    def find_element(self, locator):
        return WebDriverWait(self.driver, Configuration.time_out). \
            until(ec.presence_of_element_located(locator),
                  message=f"Can't find element by locator {locator}")

    @allure.step
    def find_elements(self, locator):
        return WebDriverWait(self.driver, Configuration.time_out). \
            until(ec.presence_of_all_elements_located(locator),
                  message=f"Can't find elements by locator {locator}")

    @allure.step
    def go_to_site(self, url):
        self.driver.get(self.base_url + url)
        return self

    @allure.step
    def go_to_site_through_token(self):
        self.driver.get(self.base_url_token)
        return self

    @allure.step
    def switch_iframe(self, locator):
        self.driver.switch_to_frame(locator)
        return self

    @allure.step
    def switch_from_iframe(self):
        self.driver.switch_to_default_content()
        return self

    @allure.step
    def screenshot(self):
        self.driver.get_screenshot_as_png()
        return self

    @allure.step
    def screenshot_for_vrt(self):
        return self.driver.get_screenshot_as_base64()

    def screenshot_check(self, vrt_name, vrt_viewport, vrt_os, vrt_device):
        config = Config(
            # apiUrl - URL where backend is running
            apiUrl=Configuration.vrt_apiUrl,
            # project - Project name or ID
            project=Configuration.vrt_project,
            # apiKey - User apiKey
            apiKey=Configuration.vrt_apiKey,
            # ciBuildId - Current git commit SHA
            ciBuildId=Configuration.vrt_ciBuildId,
            # branch - Current git branch
            branchName=Configuration.vrt_branchName,
            # enableSoftAssert - Log errors instead of exceptions
            enableSoftAssert=Configuration.vrt_enableSoftAssert,
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
        return self
