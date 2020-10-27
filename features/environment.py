from behave import fixture
from selenium import webdriver

'''driver path for chrome Brwosert'''
chrome_driver_path = 'E:/pythonn/sitecore/chromedriver.exe'


# -- FIXTURE- To pass Browser Driver to features
@fixture
def get_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(chrome_driver_path, options=options)
    context.driver.implicitly_wait(10)
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.close()