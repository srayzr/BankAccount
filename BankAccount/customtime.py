# time.py
class TimeValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class TimeTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong type for {}: {}".format(self.message, type(self.value))


class Time:
    def __init__(self, h, m, s):
        try:
            if type(h) != int:
                raise TimeTypeError("hour", h)
            elif type(m) != int:
                raise TimeTypeError("minute", m)
            elif type(s) != int:
                raise TimeTypeError("second", s)

            if h < 0 or h > 23:
                raise TimeValueError("hour", h)
            elif m < 0 or m > 59:
                raise TimeValueError("minute", m)
            elif s < 0 or s > 59:
                raise TimeValueError("second", s)
        except TimeValueError as err:
            print(err)
        except TimeTypeError as err:
            print(err)
        else:
            self.hour = h
            self.minute = m
            self.second = s

    def __repr__(self):
        try:
            return "{}:{}:{}".format(self.hour, self.minute, self.second)
        except AttributeError:
            return "Object is empty."

    def add_hour(self, n):
        try:
            if type(n) != int:
                raise TimeTypeError("param n", type(n))
            if n <= 0:
                raise TimeValueError("param n", n)
            self.hour = (self.hour + n) % 24
        except TimeValueError as err:
            print(err)
        except TimeTypeError as err:
            print(err)
        except AttributeError:
            print("Object does not have attribute 'hour'")
