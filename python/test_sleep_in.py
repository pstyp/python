pytestfrom sleep_in import sleep_in
import pytest

def test_sleep_in():
    assert sleep_in(True, True)==True