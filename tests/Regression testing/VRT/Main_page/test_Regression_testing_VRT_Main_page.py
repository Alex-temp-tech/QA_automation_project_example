import allure
import pytest


@allure.testcase("https://app.qase.io/case/AT-6")
@allure.feature("main_page")
@allure.title("test_AT_6_vrt_main_page")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_6_vrt_main_page(app):
    app.main_page() \
        .go_to_site("/") \
        .screenshot_check('test_AT_6_vrt_main_page', '1920x964', 'linux', 'selenoid')
