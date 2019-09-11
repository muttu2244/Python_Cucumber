 Feature: Show titles


Scenario: Adding videos to Favourite List
  Given I Navigate to Discovery page
        And Scroll down to popular shows
  When I Go to the last video
        And I Explore the Show
        And I click on show More
        And Again I click on show More
  Then Create a new file
        And write all the show titles and duration into the new file


