import allure
import pytest
from src import accounts
from src.pages.main_page import MainPageHelper
from src.pages.login_page import LoginPageHelper


@allure.testcase("https://app.qase.io/case/AT-6")
@allure.feature("main_page")
@allure.title("test_AT_6_vrt_main_page")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_6_vrt_main_page(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site("/")
    main_page.screenshot_check('test_AT_6_vrt_main_page', '1920x964', 'linux', 'selenoid')