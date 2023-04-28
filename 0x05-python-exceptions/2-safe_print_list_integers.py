#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_numbers = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_numbers += 1
        except (ValueError, TypeError):
            pass

    print()
    return real_numbers