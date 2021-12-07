#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements_to_print = 0

    for i in range(0, x):
        try:

            print("{:d}".format(my_list[i]), end="")
            elements_to_print += 1

        except (ValueError, TypeError):
            continue

        print()
        return (elements_to_print)
