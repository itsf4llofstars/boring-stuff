"""Chapter Seven: Pattern Matching with Regular Expressions
"""
import re

import lorem


def search_phone_numbers(search_for, search_in):
    """phone number specific"""

    # compile the text as a regex pattern
    search_regex = re.compile(search_for)

    # Search for the compiled pattern in the lorem_text variable
    found_obj = search_regex.search(search_in)

    return found_obj


def serach_for_item(search_for, search_in):
    """A more general search"""

    search_regex = re.compile(search_for)
    found_item = search_regex.search(search_in)
    return found_item


def main():
    """main function"""
    bol = (False, True)

    # Phone numbers and groups
    if bol[0]:
        """Phone number: NNN-NNN-NNNN"""
        # phone_num = r'\d\d\d-\d\d\d-\d\d\d'
        # phone_num = r'\d{3}-\d{3}-\d{4}'
        phone_num = r'(\d{3})-(\d{3}-\d{4})'  # group([|0|1|2]) brackets not needed
        # phone_num = r'\(\d{3}\)\s\d{3}-\d{4}'  # group([|0|1|2])
        # phone_num = r'(\(\d{3}\))\s(\d{3}-\d{4})'  # group([|0|1|2])

        found_obj = search_phone_numbers(phone_num, lorem.lorem_text)

        print(found_obj)
        print(found_obj.group())

        """Uncomment below to see the different groups"""
        print(found_obj.group(0))
        print(found_obj.group(1))
        print(found_obj.group(2))

        # Search for a toll free number

        foo = r'\d-\d{3}-\d{3}-\d{4}'
        bar = search_phone_numbers(foo, lorem.lorem_text)
        print(bar)

    # Using a pipe
    if bol[0]:
        white_force = r'obi wan kenobi|darth vader'
        dark_force = r'darth vader|luke skywalker'

        one = r'first|second'
        two = r'second|third'

        white_side = serach_for_item(white_force, lorem.lorem_text)
        dark_side = serach_for_item(dark_force, lorem.lorem_text)
        print(white_side)
        print(white_side.group())
        print(dark_side)
        print(dark_side.group())

        search_one = serach_for_item(one, lorem.lorem_text)
        search_two = serach_for_item(two, lorem.lorem_text)
        print(search_one)
        print(search_two)


if __name__ == '__main__':
    import sys

    sys.exit(main())
