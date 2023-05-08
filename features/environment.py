# import allure
# from allure_commons.types import AttachmentType
from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options

# from appium import webdriver

from support.logger import logger, MyListener


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_cureskin):
    """
    :param context: Behave context
    """

    # # Enable for Chrome
    # service = Service('/Users/julian.choy/PycharmProjects/Careerist/CureSkin/chromedriver')
    # context.driver = webdriver.Chrome(service=service)
    # # Enable for Chrome

    # Enable for Firefox
    # service = Service('/Users/julian.choy/PycharmProjects/Careerist/CureSkin/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # Enable for Firefox

    # # Enable for Safari
    # context.driver = webdriver.Safari()
    # # Enable for Safari

    # # Enable for headless
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    #
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=Service('/Users/julian.choy/PycharmProjects/Careerist/CureSkin/chromedriver')
    # )
    # # Enable for headless

    # # Enable for browserstack
    # bs_user = 'julianchoy_s5WALm'
    # bs_key = 'Ewaivx5jeJ5fivLVNzZn'
    #
    # desired_cap = {
    #     'browserName': 'Chrome',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_cureskin
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # # Enable for browserstack

    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
