#class MyError:
#    pass

#raise MyError()


class MyError(BaseException):
    pass

raise MyError()


class MyError(Exception):
    pass

raise MyError()