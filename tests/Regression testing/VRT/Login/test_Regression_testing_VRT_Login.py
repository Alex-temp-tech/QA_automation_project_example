# import allure
# import pytest
# from src import accounts
# from src.pages.main_page import MainPageHelper
# from src.pages.login_page import LoginPageHelper
# import time
# from src.accounts import acc
#
#
# @allure.testcase("https://app.qase.io/case/AT-7")
# @allure.feature("login")
# @allure.title("test_AT_7_vrt_main_page_click_on_the_yellow_button")
# @pytest.mark.smoke
# @allure.tag("test_UI")
# def test_AT_7_vrt_main_page_click_on_the_yellow_button(browser):
#     LoginPageHelper(browser) \
#         .go_to_site("/") \
#         .click_on_the_yellow_button()
#     LoginPageHelper(browser).screenshot_check('test_AT_7_vrt_main_page_click_on_the_yellow_button', '1920x964', 'linux', 'selenoid')
#
#
# @allure.testcase("https://app.qase.io/case/AT-8")
# @allure.feature("login")
# @allure.title("vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click")
# @pytest.mark.smoke
# @allure.tag("test_UI")
# def test_AT_8_vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click(browser):
#     LoginPageHelper(browser) \
#         .go_to_site("/") \
#         .click_on_the_yellow_button() \
#         .enter_email(acc["radwexe"]["login"]) \
#         .enter_password(acc["radwexe"]["pass"])
#     LoginPageHelper(browser).screenshot_check('test_AT_8_vrt_main_page_modal_window_top_right_button_with_valid_credentials_before_click',
#                           '1920x964', 'linux', 'selenoid')
