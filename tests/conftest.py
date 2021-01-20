import configparser
import os
import sys
import pytest
from selenium import webdriver
from src import browsers
import allure
from allure_commons.types import AttachmentType

def read_ini():
    config_file_name = os.environ.get("config-file", 'project-config.ini')
    root_path = os.path.join(sys.path[1], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser

def get_confg():
    return read_ini()

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
            command_executor=get_confg()['DEFAULT']['ip_selenoid_serv'],
            desired_capabilities=capabilities)
    elif selenoid == "mac":
        browser = webdriver.Remote(
            command_executor=get_confg()['DEFAULT']['ip_selenoid_mac'],
            desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--selenoid should be mac or serv")

    browser.maximize_window()
    browser.implicitly_wait(get_confg()['DEFAULT']['tout'])
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()
