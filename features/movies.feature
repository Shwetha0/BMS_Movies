Feature: Movies

  Scenario: Book a movie
    Given launch chrome browser
    When Open BookMyShow homepage
    Then Choose location
    And Click on Movies button
    And Choose English
    And Choose a movie
    And Click on BookTickets button
    And Choose 3D
    And Choose date
    And Choose showtimings
    And Accept Terms and Conditions
    And Select no of seats
    And Click on Selectseats
    And Select desired seat
    And Click on Pay button
    And Close browser
