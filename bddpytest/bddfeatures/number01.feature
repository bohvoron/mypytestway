Feature: Transaction Bank Acc
    Tests pertaining to banks Transactions (like withdrawal, deposit and etc)
    

    Scenario: Withdrawal of money
        Given The balance is 1000
        When the acc holder withdraws 300
        Then balans should to be 700
 
    Scenario: Remove fruits with set
        Given have set of 4 fruits
        When We remove 1 fruit from a set
        Then finall set has 3 fruits

