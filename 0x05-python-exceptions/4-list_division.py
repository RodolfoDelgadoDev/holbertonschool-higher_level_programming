#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result = 0
    f = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new.append(result)
        except IndexError:
            print("out of range")
            new.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        finally:
            f = f
    return new
