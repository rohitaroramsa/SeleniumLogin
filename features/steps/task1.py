from features.environment import get_browser
from behave import given, when, then, use_fixture
from pages.google import googleSearch
import time


@given(u'A Chrome Browser')
def step_impl(context):
    context.driver = use_fixture(get_browser, context)
    context.g1 = googleSearch(context.driver)


@when(u'user browses site "{url}"')
def step_impl(context, url):
    context.driver.get(url)   #to browse site
    context.g1.accept_agreement()   # Google's I Agreement button


@when(u'user enters "{cityname}"')
def step_impl(context, cityname):
    context.g1.search_box(cityname)
    context.city_name = cityname  # city name is used further for verifying Title + saving screenshot


@when(u'user clicks on Search button')
def step_impl(context):
    context.g1.search_click()
    time.sleep(2)


@then(u'the search result Page should open')
def step_impl(context):
    assert context.driver.title == context.city_name + ' - Google Search'


@then(u'screenshot shall be taken')
def step_impl(context):
    screenshot_file = 'captured_screenshots/' + context.city_name + '.png'
    context.driver.save_screenshot(screenshot_file)