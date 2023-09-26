import getopt
import sys

from coll_aoc_runner.aoc_delimiter import AoCDelimiter
from coll_aoc_runner.aoc_runner import AoCRunner
from coll_aoc_runner.aoc_years import AoCYears

from years import *


def main():
    delimiter = get_commandline_options()

    runner = AoCRunner(set_years)
    runner.run(delimiter)


def get_commandline_options() -> AoCDelimiter:
    delimiter = AoCDelimiter()

    optlist, args = getopt.getopt(sys.argv[1:], "y:d:p:")

    for index in range(len(optlist)):
        if optlist[index] == 'y':
            delimiter.year = int(args[index])
        elif optlist[index] == 'd':
            delimiter.day = int(args[index])
        elif optlist[index] == 'p':
            delimiter.part = int(args[index])


    if delimiter.year != -1 and delimiter.year < 2015:
        print("\033[33mNo Advent of Code before _2015.\033[0m")
        quit(1)
    elif delimiter.day != -1 and (delimiter.day < 1 or delimiter.day > 25):
        print("\033[31mInvalid argument for day please only use the days from 1 to 25.\033[0m")
        quit(1)
    elif delimiter.part != -1 and (delimiter.part < 1 or delimiter.part > 2):
        print("\033[31mInvalid argument for part please only use 1 or 2.\033[0m")
        quit(1)

    return delimiter


if __name__ == "__main__":
    main()


def set_years(years: AoCYears):
    pass
