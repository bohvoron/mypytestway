Feature: Parameterizing in Pytest BDD

    Scenario: Parametrize showcase
        Given 4 variaties cars 
        When add same variaty
        Then same count of cars
        But if we add a some different variaty
        Then Count increases to 5 