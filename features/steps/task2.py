from behave import given, when, then, use_fixture
from pages.expediaSearch import ExpediaPackage
from features.environment import get_browser
import time


@given(u'user opens chrome browser')
def step_impl(context):
    context.driver = use_fixture(get_browser, context)


@when(u'user goes to expedia website "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.page1 = ExpediaPackage(context.driver)


@when(u'User select option of packages')
def step_impl(context):
    context.page1.direct_package_page()


@when(u'user selects cities as "{source_city}" and "{target_city}"')
def step_impl(context, source_city, target_city):
    context.page1.set_source_city(source_city)
    context.page1.set_destination_city(target_city)


@when(u'user selects dates')
def step_impl(context):
    context.page1.set_dates()


@when(u'user select adult as 1 children as 1 of 3 year old')
def step_impl(context):
    context.page1.set_travellers()


@when(u'user clicks on Search flight button')
def step_impl(context):
    context.page1.click_search_button()


@then(u'Search results should appear')
def step_impl(context):
    time.sleep(20)
    step1_value = context.page1.get_step1_search_results_page()
    expected_value = 'Current: Step 1 of 4 select your hotel'
    assert step1_value == expected_value
    screenshot_file = 'captured_screenshots/ExpediaSearch.png'
    context.driver.save_screenshot(screenshot_file)
