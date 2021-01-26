import configparser
import os
import sys
import pytest
from selenium import webdriver
from src import browsers
import allure
from allure_commons.types import AttachmentType
from src.app import App
from configuration import Configuration


def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store', default='mac',
                     help="Choose selenoid type: serv or mac")
    parser.addoption('--br_type', action='store', default='chrome',
                     help="Choose br_type type: chrome, firefox or opera")

@pytest.fixture(scope="function")
def browser(request):
    br_type = request.config.getoption("br_type")
    if br_type == "chrome":
        capabilities = browsers.chrome
    elif br_type == "firefox":
        capabilities = browsers.firefox
    elif br_type == "opera":
        capabilities = browsers.opera
    else:
        raise pytest.UsageError("--br_type Choose should be chrome, firefox or opera")

    selenoid = request.config.getoption("selenoid")
    if selenoid == "serv":
        browser = webdriver.Remote(
            command_executor=Configuration.ip_selenoid_serv,
            desired_capabilities=capabilities)
    elif selenoid == "mac":
        browser = webdriver.Remote(
            command_executor=Configuration.ip_selenoid_mac,
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")

    browser.maximize_window()
    browser.implicitly_wait(Configuration.time_out)
    yield browser
    #allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()

@pytest.fixture(scope="function")
def app(browser):
    yield App(browser)

#If our test fall ad screenshon to allure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

