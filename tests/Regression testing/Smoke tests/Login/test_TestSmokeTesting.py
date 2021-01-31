import allure
import pytest
from src.accounts import acc
from configuration import Configuration


@allure.testcase("https://app.qase.io/case/AT-1")
@allure.feature("login")
@allure.title("test_AT_1_login_from_main_page_with_valid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_1_login_from_main_page_with_valid_credentials(app):
    app.main_page() \
        .go_to_site("/") \
        .full_login(acc[Configuration.acc_for_test]) \
        .login_check()


@allure.testcase("https://app.qase.io/case/AT-2")
@allure.feature("login")
@allure.title("test_AT_2_login_from_main_page_with_invalid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_2_login_from_main_page_with_invalid_credentials(app):
    app.main_page() \
        .go_to_site("/") \
        .full_login(acc[Configuration.acc_for_invalid]) \
        .check_invalid_credentials()


@allure.testcase("https://app.qase.io/case/AT-3")
@allure.feature("login")
@allure.title("test_AT_3_login_from_login_page_with_valid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_3_login_from_login_page_with_valid_credentials(app):
    app.login_page() \
        .go_to_site("/login") \
        .full_login(acc[Configuration.acc_for_test]) \
        .login_check()


@allure.testcase("https://app.qase.io/case/AT-4")
@allure.feature("login")
@allure.title("test_AT_4_login_from_login_page_with_invalid_credentials")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_4_login_from_login_page_with_invalid_credentials(app):
    app.login_page() \
        .go_to_site("/login") \
        .full_login(acc[Configuration.acc_for_invalid]) \
        .check_invalid_credentials()


@allure.testcase("https://app.qase.io/case/AT-5")
@allure.feature("login")
@allure.title("test_AT_5_login_from_token")
@pytest.mark.smoke
@allure.tag("test_UI")
def test_at_5_login_from_token(app):
    app.main_page() \
        .go_to_site_through_token() \
        .login_check()
