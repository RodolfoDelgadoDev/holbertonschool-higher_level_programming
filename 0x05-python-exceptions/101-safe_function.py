#!/usr/bin/python3
def safe_function(fct, *args):
    result = 0
    for i in range(1, len(args))
    try:
        result = fct(args[i])
    except TypeError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except ZeroDivisionError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except NameError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    except IndexError as err:
        print("Exception:", err, file=sys.stderr)
        return None
    return result
