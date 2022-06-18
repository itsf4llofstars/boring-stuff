"""Chapter Seven: Pattern Matching with Regular Expressions
"""
import re
import lorem


def search_phone_numbers(search_for, search_in):
    # compile the text as a regex pattern
    search_regex = re.compile(search_for)

    # Search for the compiled pattern in the lorem_text variable
    found_obj = search_regex.search(search_in)

    return found_obj


def main():
    """main function"""

    # Phone number: NNN-NNN-NNNN
    phone_num = r'\d\d\d-\d\d\d-\d\d\d'
    # phone_num = r'\d{3}-\d{3}-\d{4}'
    # phone_num = r'(\d{3})-(\d{3}-\d{4})'  # group([|0|1|2]) brackets not needed
    # phone_num = r'\(\d{3}\)\s\d{3}-\d{4}'  # group([|0|1|2])
    # phone_num = r'(\(\d{3}\))\s(\d{3}-\d{4})'  # group([|0|1|2])

    found_obj = search_phone_numbers(phone_num, lorem.lorem_text)

    print(found_obj)
    print(found_obj.group())
    print(found_obj.group(0))
    print(found_obj.group(1))
    print(found_obj.group(2))


if __name__ == '__main__':
    import sys

    sys.exit(main())
