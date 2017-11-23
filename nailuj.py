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

    jdn1 = JulianDayNumber("en")
    jdn1.set_ymd(today_year, today_month, today_day)
    today_jdn = jdn1.get_jdn()

    program_name = sys.argv[0]
    # print "program_name: " + program_name

    parser = argparse.ArgumentParser(description='Accept a JDN.')

    parser.add_argument('jdn', type=int, nargs='?',\
            default=today_jdn, help='Julian Day Number')

    args = parser.parse_args()
    jdn1.set_jdn(args.jdn)

    day_of_week = jdn1.get_day_of_week()
    daynames = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    print "JDN is: " + str(jdn1.get_jdn())
    print "Date is: " + daynames[day_of_week] + ", " +\
            str(jdn1.get_day()) + " " +\
            jdn1.get_monthname() + " " +\
            str(jdn1.get_year())

if __name__ == '__main__':
    main()
