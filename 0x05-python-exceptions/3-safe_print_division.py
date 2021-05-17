#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        result = None
    except TypeError:
        print("Inside result: {}".format(None))
        result = None
    except NameError:
        print("Inside result: {}".format(None))
        result = None
    finally:
        return result
