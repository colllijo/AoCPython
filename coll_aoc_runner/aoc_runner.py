import os

from coll_aoc_runner.aoc_delimiter import AoCDelimiter
from coll_aoc_runner.aoc_input import AoCInput
from coll_aoc_runner.aoc_years import AoCYears


class AoCRunner:
    def __init__(self, set_years):
        self.aoc_years = AoCYears()
        self.aoc_input = AoCInput()

        set_years(self.aoc_years)

    def run(self, delimiter: AoCDelimiter):
        if delimiter.year == -1 or delimiter.day == -1:
            delimiter.part = -1

        for day in self.get_days_to_run(delimiter).values():
            input = self.aoc_input.get_input(day.year, day.day)

            if delimiter.part == 1:
                self.run_part(AoCDelimiter(day.get_year(), day.get_day(), 1), day.part_1(input))
            elif delimiter.part == 2:
                self.run_part(AoCDelimiter(day.year, day.day, 2), day.part_2(input))
            else:
                self.run_part(AoCDelimiter(day.year, day.day, 1), day.part_1(input))
                self.run_part(AoCDelimiter(day.year, day.day, 2), day.part_2(input))

    def run_part(self, delimiter: AoCDelimiter, result: str):
        if result:
            print(
                f"\033[92m*** Part {delimiter.part} of day {delimiter.day} in year {delimiter.year} Result: {result}\033[0m")

            os.system(f"echo -n {result.strip()} | clip.exe");

    def get_days_to_run(self, delimiter: AoCDelimiter):
        days_to_run = {}

        if delimiter.year != -1:
            if delimiter.day != -1:
                day = self.aoc_years.get_day(delimiter.year, delimiter.day)

                if day is not None:
                    days_to_run.update({len(days_to_run.keys()): day})
            else:
                days = self.aoc_years.get_year(delimiter.year)
                if days is not None:
                    for day_index in days.get_days():
                        day = self.aoc_years.get_day(delimiter.year, day_index)
                        if day is not None:
                            days_to_run.update({len(days_to_run.keys()): day})
        else:
            for year_index in self.aoc_years.get_years():
                for day_index in self.aoc_years.get_year(year_index).get_days():
                    day = self.aoc_years.get_day(year_index, day_index)
                    if day is not None:
                        days_to_run.update({len(days_to_run.keys()): day})

        return days_to_run
