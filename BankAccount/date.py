class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_NAMES = [
        "",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def __repr__(self):
        return "{} {} {}".format(self.day, self.MONTH_NAMES[self.month], self.year)

    def add_year(self, n=1):
        self.year += n

    def add_month(self, n=1):
        self.add_year((self.month + n - 1) // 12)
        self.month = (self.month + n - 1) % 12 + 1

    def add_day(self, n=1):
        self.add_month((self.day + n - 1) // 30)
        self.day = (self.day + n - 1) % 30 + 1
