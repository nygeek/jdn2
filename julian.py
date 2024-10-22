#!/usr/bin/python

""" julian.py

Compute the Julian Day Number for a date.  Accept
a date (Y, M, D) on the command line and return the
Julian Day Number.

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

    _program_name = sys.argv[0]
    # print "_program_name: " + _program_name

    parser = argparse.ArgumentParser(description='Accept a date. [Python2]')

    parser.add_argument('year', type=int, nargs='?',\
            default=today_year, help='Year number')
    parser.add_argument('month', type=int, nargs='?',\
            default=today_month, help='Month number')
    parser.add_argument('day', type=int, nargs='?',\
            default=today_day, help='Day number')

    args = parser.parse_args()

    # print "Year"
    # print args.year
    # print "Month"
    # print args.month
    # print "Day"
    # print args.day

    engine = JulianDayNumber("en")
    engine.set_ymd(args.year, args.month, args.day)
    dow_name = engine.get_dow_name()

    print "Date is: " + dow_name + ", " +\
            str(engine.get_day()) + " " +\
            engine.get_monthname() + " " +\
            str(engine.get_year())
    print "JDN is: " + str(engine.get_jdn())

if __name__ == '__main__':
    main()
