Feature: Scenario outline
    similar to Parameterizing
   
   Scenario Outline: Test with Outline
        Given There are <start> cars
        When I deposit <deposit> cars
        And I withdraw <withdraw> cars
        Then I have <finall> cars
        
        Examples: 
        |  start  |  deposit  |  withdraw  |  finall  | 
        | value 1 |     5     |     7      |   10     |
        | value 2 |     5     |     20     |   -5     |
     
 