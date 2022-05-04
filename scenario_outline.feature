Feature: Feature eating
    Scenario Outline: eating 
        Given there are <start> cucumbers
        When I eat <eat> cucumbers
        Then I have <left> cucumbers
        Examples: 
        |start  |eat    |left    |
        |10     |6      |1      |
        |11     |6      |2       |

