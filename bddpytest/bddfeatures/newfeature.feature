Feature: Fixture and Bdd Background on python set Datatype


    Background: Seting data before test
    Given datatype is set
    And set is not empty

    Scenario: Adding to a Set
    Given A set has 3 elem
    When Add 2 elem to set 
    Then total is 5 elem