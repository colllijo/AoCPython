from coll_aoc_runner.aoc_day import AoCDay
from coll_aoc_runner.aoc_days import AoCDays

class AoCYears:
    def __init__(self):
        self.years = {}

    def set_year(self, year: int, aoc_year: AoCDays):
        self.years.update({year: aoc_year})

    def get_year(self, year: int) -> AoCDays:
        return self.years.get(year)

    def get_years(self):
        return self.years.keys()

    def set_day(self, year: int, day: int, aoc_day: AoCDay):
        if self.get_year(year) is None:
            self.years.update({year: AoCDays()})

        self.get_year(year).set_day(day, aoc_day)

    def get_day(self, year: int, day: int) -> AoCDay:
        return self.get_year(year).get_day(day)