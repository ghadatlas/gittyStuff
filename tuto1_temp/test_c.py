from pytest_bdd import given, when, then, scenario, parsers
import re


@scenario(
    "outline.feature",
    "Outlined given, when, then",
)
def test_outlined():
    pass


@given(parsers.parse("there are {start:d} cucumbers", target_fixture="start_cucumbers"))
def start_cucumbers(start):
    assert isinstance(start, int)
    return dict(start=start)


@when(parsers.parse("I eat {eat:g} cucumbers"))
def eat_cucumbers(start_cucumbers, eat):
    assert isinstance(eat, float)
    start_cucumbers["eat"] = eat


@then(parsers.parse("I should have {left} cucumbers"))
def should_have_left_cucumbers(start_cucumbers, start, eat, left):
    assert isinstance(left, str)
    assert start - eat == int(left)
    assert start_cucumbers["start"] == start
    assert start_cucumbers["eat"] == eat