import re 
from pytest_bdd import scenario, given, when, then, parsers
@scenario("scenario_outline.feature", "eating")
def test_scen():
    print("my scenario")
@given(
    parsers.parse("there are {start:d} cucumbers"), target_fixture="init_cucumber")
def init_cucumber(start):
    assert isinstance(start,int)
    print(start)
@when(
    parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumber(eat):
    pass 
@then(
    parsers.parse("I have {left:d} cucumbers"))
def init_cucumber(start,eat, left):
    assert start-eat==left
    print(left)