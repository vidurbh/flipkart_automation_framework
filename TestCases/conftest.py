
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="Edge":
        driver=webdriver.Ie()

    elif browser=="Firefox":
        driver=webdriver.Firefox()

    elif browser=="Chrome":
        driver=webdriver.Chrome()

    else :
        print("No browser given")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
