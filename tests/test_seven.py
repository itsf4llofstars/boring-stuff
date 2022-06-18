"""Test file for seven.py file using pytest
"""
from src.chapters.seven.seven import search_phone_numbers
from src.chapters.seven.seven import search_for_item


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


def test_search_phone_numbers_three():
    test_str = 'My phone is (123) 555-2357 call soon'
    find = r'\(\d{3}\)\s(\d{3}-\d{4})'
    found = search_phone_numbers(find, test_str)
    assert found.group() == '(123) 555-2357'


def test_search_phone_numbers_four():
    test_str = 'My phone is (123) 555-2357 call soon'
    find = r'\(\d{3}\)\s(\d{3}-\d{4})'
    found = search_phone_numbers(find, test_str)
    assert found.group(0) == '(123) 555-2357'


def test_search_phone_numbers_five():
    test_str = 'My phone is (123) 555-2357 call soon'
    find = r'(\(\d{3}\))\s(\d{3}-\d{4})'
    found = search_phone_numbers(find, test_str)
    assert found.group(1) == '(123)'


def test_search_phone_numbers_six():
    test_str = 'My phone is (123) 555-2357 call soon'
    find = r'(\(\d{3}\))\s(\d{3}-\d{4})'
    found = search_phone_numbers(find, test_str)
    assert found.group(2) == '555-2357'


def test_search_for_item_butter():
    test_str = 'bacon butter beans ham spam and eggs'
    find = r'butter|spam'
    found = search_for_item(find, test_str)
    assert found.group() == 'butter'


def test_search_for_item_spam():
    test_str = 'bacon butter beans ham spam and eggs'
    find = r'spam|butter'
    found = search_for_item(find, test_str)
    assert found.group() == 'butter'


def test_search_for_item_beans():
    test_str = 'bacon butter beans ham spam and eggs'
    find = r'beans|chicken'
    found = search_for_item(find, test_str)
    assert found.group() == 'beans'


def test_search_for_item_chicken():
    test_str = 'bacon butter beans ham spam and eggs'
    find = r'chicken|beans'
    found = search_for_item(find, test_str)
    assert found.group() == 'beans'


def test_search_for_item_batman():
    test_str = 'bacon batman beans batwoman and eggs'
    find = r'bat(wo)?man'
    found = search_for_item(find, test_str)
    assert found.group() == 'batman'


def test_search_for_item_batwoman():
    test_str = 'bacon batwoman beans batman and eggs'
    find = r'bat(wo)?man'
    found = search_for_item(find, test_str)
    assert found.group() == 'batwoman'


def test_search_for_item_sha():
    test_str = 'Git uses a sha number, but shanana is a band.'
    find = r'sha(na)*'
    found = search_for_item(find, test_str)
    assert found.group() == 'sha'


def test_search_for_item_shanana():
    test_str = 'The group shanana may not know of Git sha numbers.'
    find = r'sha(na)*'
    found = search_for_item(find, test_str)
    assert found.group() == 'shanana'


def test_search_for_item_greed():
    test_str = 'funny hahahahahahahaha'  # 8
    find = r'(ha){3,6}'
    found = search_for_item(find, test_str)
    assert found.group() == 'hahahahahaha'


def test_search_for_item_nongreed():
    test_str = 'funny hahahahahahahaha'  # 8
    find = r'(ha){3,6}?'
    found = search_for_item(find, test_str)
    assert found.group() == 'hahaha'
