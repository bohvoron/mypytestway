Feature: Scenario outline
    similar to Parameterizing
   
   Scenario Outline: Test with Outline
        Given There are <start> cars
        When I deposit <deposit> cars
        And I withdraw <withdraw> cars
        Then I have <finall> cars
        
        Examples: 
        |  start  |  deposit  |  withdraw  |  finall  | 
        |   20    |     5     |     7      |   18     |
        |   10    |     9     |     20     |   -1     |
     
 