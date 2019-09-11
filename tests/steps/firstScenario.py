from behave import given, when, then
from framework.webapp import webapp


@given(u'I Navigate to Discovery page')
def step_impl_load_website(context):
    webapp.load_website()
    #And Scroll down to popular shows

    #webapp.scroll_page()


@when(u'I Go to the last video')
def step_impl_goto_page(context, page):
    webapp.goto_page()
    #And I Explore the Show
    webapp.explore_show_more()
    #And I click on show More
    #And Again I click on show More


@then(u'Create a new file')
def step_create_new_file(context, component):
    webapp.create_file(component)
    #And write all the show titles and duration into the new file
