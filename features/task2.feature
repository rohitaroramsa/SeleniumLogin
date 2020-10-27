Feature: Selection of Flights over Expedia website

  Scenario: User should be able to search flight + Stay at Expedia

    Given user opens chrome browser
    When user goes to expedia website "https://www.expedia.com"
    and User select option of packages
    and user selects cities as "Brussels" and "New York"
    and user selects dates
    and user select adult as 1 children as 1 of 3 year old
    and user clicks on search flight button
    Then Search results should appear