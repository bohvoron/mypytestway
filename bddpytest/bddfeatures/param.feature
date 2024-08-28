Feature: Parameterizing in Pytest BDD

    Scenario: Parametrize showcase
        Given 4 variaties cars 
        When add same variaty
        Then same count of cars
        But if we add a some different variaty
        Then Count increases to 5 
    
    Scenario: Parametrize benefits 
        Given Given a 5 cars
        When I gave 3 cars to cousin
        And I gave 2 cars to cousin 
        Then I have 0 cars for gifts