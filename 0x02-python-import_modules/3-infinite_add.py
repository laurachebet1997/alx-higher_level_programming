#!/usr/bin/python3


def add_arg(argv):
    nlength = len(argv) - 1
    if nlength == 0:
        print("{:d}".format(nlength))
        return
    else:
        i = 1
        add = 0
        while i < nlength:
            add += int(argv[i])
            i += 1
            print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
