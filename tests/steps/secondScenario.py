from behave import given, when, then
from framework.webapp import webapp


@given(u'Given I am on the Discovery my videos page')
def step_impl_load_website(context):
    webapp.load_website()


@when(u'When I search videos ')
def step_impl_goto_page(context, page):
    webapp.goto_page(page)


@then(u'Then I should see correct video title and description "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
