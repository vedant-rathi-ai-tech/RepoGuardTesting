# tests/test_repair_guardrail_demo.py

from repair_guardrail_demo import (
    get_first_value,
    get_second_value,
    get_third_value,
)


def test_first_value():
    assert get_first_value() == "correct_one"


def test_second_value():
    assert get_second_value() == "correct_two"


def test_third_value():
    assert get_third_value() == "correct_three"
