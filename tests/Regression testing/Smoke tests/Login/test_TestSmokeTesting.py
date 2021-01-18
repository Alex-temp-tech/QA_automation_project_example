import allure
import pytest
from src import accounts
from src.pages.main_page import MainPageHelper
from src.pages.login_page import LoginPageHelper


@allure.testcase("https://app.qase.io/case/AT-1")
@allure.feature("login")
@allure.title("test_AT_1_login_from_main_page_with_valid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_1_login_from_main_page_with_valid_credentials(browser):
   main_page = MainPageHelper(browser)
   main_page.go_to_site("/")

   main_page.full_login(accounts.acc["radwexe"])
   main_page.login_check()

@allure.testcase("https://app.qase.io/case/AT-2")
@allure.feature("login")
@allure.title("test_AT_2_login_from_main_page_with_invalid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_2_login_from_main_page_with_invalid_credentials(browser):
   main_page = MainPageHelper(browser)
   main_page.go_to_site("/")
   main_page.full_login(accounts.acc["radwexe_invalid"])
   main_page.check_invalid_credentials()

@allure.testcase("https://app.qase.io/case/AT-3")
@allure.feature("login")
@allure.title("test_AT_3_login_from_login_page_with_valid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_3_login_from_login_page_with_valid_credentials(browser):
   login_page = LoginPageHelper(browser)
   login_page.go_to_site("/login")
   login_page.full_login(accounts.acc["radwexe"])
   login_page.login_check()

@allure.testcase("https://app.qase.io/case/AT-4")
@allure.feature("login")
@allure.title("test_AT_4_login_from_login_page_with_invalid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_4_login_from_login_page_with_invalid_credentials(browser):
   login_page = LoginPageHelper(browser)
   login_page.go_to_site("/login")
   login_page.full_login(accounts.acc["radwexe_invalid"])
   login_page.check_invalid_credentials()

@allure.testcase("https://app.qase.io/case/AT-5")
@allure.feature("login")
@allure.title("test_AT_5_login_from_token")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_AT_5_login_from_token(browser):
   test_login_from_token = MainPageHelper(browser)
   test_login_from_token.go_to_site_through_token()
   test_login_from_token.login_check()
