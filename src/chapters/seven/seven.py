"""Chapter Seven: Pattern Matching with Regular Expressions
"""
import re

BOL = (False, True)

LOREM = (
    "Sit maiores recusandae ipsum nihil amet iste. Et illo at nulla quaerat\n"
    "assumenda. Quis phone 232-555-2341 aesentium corrupti laboriosam placeat\n"
    "voluptatem? Dolore repellat commodi phone (323) 555-8762 incidunt Quod\n"
    "possimus ex fugiat iusto et nostrum. Mollitia repellendus ut nostrum molestias\n"
    "saepe Eaque quibusdam sapiente nihil facere ut. Aspernatur voluptas quod omnis\n"
    "ratione recusandae Vitae odit ipsam distinctio eius excepturi aspernatur ad!\n"
    "Illum dicta consequuntur velit dignissimos nisi. Quis fugit quo dolorem\n"
    "asperiores nulla. Impedit aspernatur eligendi dolorem doloremque qui quisquam!\n"
    "Numquam ipsam quis est reprehenderit ipsa. Commodi culpa fugit dolorem at\n"
    "distinctio corrupti. Quisquam sequi odio reprehenderit quidem in Assumenda\n"
    "distinctio repellendus aliquam libero rerum. Voluptas excepturi laboriosam\n"
    "ratione rem necessitatibus Ex corporis soluta ab quibusdam amet rem! Ducimus\n"
    "laborum obi wan kenobi ipisci quae vero culpa. Eveniet ea architecto amet\n"
    "reiciendis repellat commodi? Velit ab sequi magnam aperiam earum. Aspernatur\n"
    "est minus deserunt third ore provident Vel darth vader llo autem aliquam\n"
    "voluptas quis esse, omnis. Cupiditate first sciunt rem nostrum est quaerat Id\n"
    "unde sed culpa recusandae voluptate? Ea consectetur dicta dolore excepturi\n"
    "dignissimos? Dolores iste quisquam dolor dignissimos obcaecati. Doloribus sint\n"
    "quas harum qui eum explicabo A pariatur ipsa placeat laudantium eveniet\n"
    "Ducimus alias nam dolorem nemo molestias. Dolorem perspiciatis voluptatem\n"
    "accusamus repellendus dolores Velit beatae nostrum earum ad laboriosam ad Hic\n"
    "et nemo suscipit libero laboriosam Saepe magnam harum expedita ducimus culpa\n"
    "minima odit nihil, est. Minus recusandae vero nobis luke skywalker Perferendis\n"
    "vel 1-800-555-3453 bero quaerat iure laudantium. In culpa minus odio libero\n"
    "expedita? Incidunt qui odio praesentium perferendis delectus. Consectetur rem\n"
    "perferendis veniam possimus iure perspiciatis! Autem animi doloremque at\n"
    "voluptas minus Aspernatur totam molestias esse dolores perferendis. Numquam\n"
    "voluptatibus soluta aut ipsa amet In tenetur aliquid id quos excepturi Eius\n"
    "architecto libero deserunt suscipit second unt Molestiae quisquam suscipit\n"
    "dolore ipsa aperiam Similique rem iste quas modi\n"
)


def search_phone_numbers(search_for, search_in):
    """phone number specific"""

    # compile the text as a regex pattern
    search_regex = re.compile(search_for)

    # Search for the compiled pattern in the lorem_text variable
    found_obj = search_regex.search(search_in)

    return found_obj


def serach_for(search_for, search_in):
    """A more general search"""

    search_regex = re.compile(search_for)
    found_item = search_regex.search(search_in)
    return found_item


def main():
    """main function"""
    global LOREM, BOL

    # Phone numbers and groups
    if BOL[0]:
        """Phone number: NNN-NNN-NNNN"""
        # phone_num = r'\d\d\d-\d\d\d-\d\d\d\d'
        # phone_num = r'\d{3}-\d{3}-\d{4}'
        # phone_num = r'\(\d{3}\)\s\d{3}-\d{4}'

        # phone_num = r'(\d{3})-(\d{3}-\d{4})'  # group([|0|1|2]) brackets not needed
        phone_num = r'(\(\d{3}\))\s(\d{3}-\d{4})'  # group([|0|1|2])

        found_obj = search_phone_numbers(phone_num, LOREM)

        print(found_obj)
        print(found_obj.group())

        """Uncomment below to see the different groups"""
        print(found_obj.group(0))
        print(found_obj.group(1))
        print(found_obj.group(2))

        # Search for a toll-free number
        foo = r'\d-\d{3}-\d{3}-\d{4}'
        bar = search_phone_numbers(foo, LOREM)
        print(bar)

    # Using a pipe
    if BOL[0]:
        white_force = r'obi wan kenobi|darth vader'
        dark_force = r'darth vader|luke skywalker'

        one = r'first|second'
        two = r'second|third'
        three = r'first|third'

        white_side = serach_for(white_force, LOREM)
        dark_side = serach_for(dark_force, LOREM)
        print(white_side)
        print(dark_side)
        print(white_side.group())
        print(dark_side.group())

        search_one = serach_for(one, LOREM)
        search_two = serach_for(two, LOREM)
        search_three = serach_for(three, LOREM)
        print(search_one)
        print(search_two)
        print(search_three)
        print(search_one.group())
        print(search_two.group())
        print(search_three.group())


if __name__ == '__main__':
    import sys

    sys.exit(main())
