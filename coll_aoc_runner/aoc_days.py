from coll_aoc_runner.aoc_day import AoCDay


class AoCDays:
    def __init__(self):
        self.days = {}

    def set_day(self, day: int, aoc_day: AoCDay):
        self.days.update({day: aoc_day})

    def get_day(self, day: int) -> AoCDay:
        return self.days.get(day)

    def get_days(self):
        return self.days.keys()
