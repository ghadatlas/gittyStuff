import re 
from pytest_bdd import scenario, given, when, then, parsers
@scenario("scenario_outline.feature", "eating")
def test_scen():
    pass
@given(
    parsers.parse("there are {start:d}"), target_fixture="start_cucumber")
def start_cucumber(start):
    print(start)
@when(
    parsers.parse("I eat {eat:d}"), target_fixture="eat_cucumber")
def eat_cucumber(eat):
    print(eat)
@then(
    parsers.parse("I have {left:d}"), target_fixture="left_cucumber")
def left_cucumber(left):
        print(left)