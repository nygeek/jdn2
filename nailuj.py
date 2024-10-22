#!/usr/bin/python

""" julian.py

Compute the Gregorian date for a JDN.  Accept a JDN in the command
line argument and return Y, M, and D

"""

from datetime import date
import argparse
import sys
from jdn import JulianDayNumber

def main():
    """main routine."""

    # get the current year, month, and day
    today = date.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day

    engine = JulianDayNumber("en")
    engine.set_ymd(today_year, today_month, today_day)
    today_jdn = engine.get_jdn()

    _program_name = sys.argv[0]
    # print "_program_name: " + _program_name

    parser = argparse.ArgumentParser(description='Accept a JDN.  [Python2]')

    parser.add_argument('jdn', type=int, nargs='?',\
            default=today_jdn, help='Julian Day Number')

    args = parser.parse_args()
    engine.set_jdn(args.jdn)

    dow_name = engine.get_dow_name()

    print "JDN is: " + str(engine.get_jdn())
    print "Date is: " + dow_name + ", " +\
            str(engine.get_day()) + " " +\
            engine.get_monthname() + " " +\
            str(engine.get_year())

if __name__ == '__main__':
    main()
