Feature: A dictionary with advanced default value handling
    As a Python guru
    In order to mitigate the shortcomings of collections.defaultdict
    I shall implement defaultdict2

    Scenario: Assignment
        Given I have an increment-by-one defaultdict2
        When I assign the value 7 to the key 5
        Then it should contain the key 5
        And I should be able to retrieve the value 7 for the key 5

    Scenario: Default value
        Given I have an increment-by-one defaultdict2
        Even though it does not contain the key 6
        Still I should be able to retrieve the value 7 for the key 6

    Scenario: Dictiness
        Given I have an increment-by-one defaultdict2
        After I insert some values
            | key       | value |
            | 1         | 5     |
            | 2         | 7     |
            | 3         | 10    |
        Then it should look like {1:5,2:7,3:10}
