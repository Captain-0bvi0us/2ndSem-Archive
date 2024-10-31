Feature: sortArray

Scenario: let`s sort our array
    Given I have the array
    When the array is sorting
    Then the array is sorted

Scenario: let`s sort array with some same numbers
    Given I have the array with some same numbers
    When the array with same same numbers is sorting
    Then the array with same same numbers is sorted

Scenario: let`s sort the empty array
    Given I have the empty array
    When the empty array is sorting
    Then the empty array is sorted
