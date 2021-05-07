#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    con = 0
    rev = False
    lon = len(roman_string)
    for n in range(lon):
        if rev is True:
            rev = False
            if n < lon:
                continue
            else:
                break
        if n < lon - 1:
            if ro.get(roman_string[n+1]) > ro.get(roman_string[n]):
                con = con + ro.get(roman_string[n + 1]) - ro.get(roman_string[n])
                rev = True
            else:
                con = con + ro.get(roman_string[n])
        else:
            con = con + ro.get(roman_string[n])
    return con
