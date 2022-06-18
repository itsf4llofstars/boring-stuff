"""Test file for seven.py file using pytest
"""
from src.chapters.seven.seven import search_phone_numbers


def test_search_phone_numbers_one():
    test_str = 'My phone is 123-555-2357 call soon'
    find = r'\d\d\d-\d\d\d-\d\d\d\d'
    found = search_phone_numbers(find, test_str)
    assert found.group() == '123-555-2357'


def test_search_phone_numbers_two():
    test_str = 'My phone is 123-555-2357 call soon'
    find = r'\d{3}-\d{3}-\d{4}'
    found = search_phone_numbers(find, test_str)
    assert found.group() == '123-555-2357'
