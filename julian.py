""" julian.py

Compute the Julian Day Number for a date.  Accept
a date (Y, M, D) on the command line and return the
Julian Day Number.

"""

from datetime import date
import argparse
from jdn import JulianDayNumber
import sys

def main():
    """main routine."""

    program_name = sys.argv[0]
    # print "program_name: " + program_name

    # get the current year, month, and day
    today = date.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day
    # print "Today: " + str(today_year) + ", " + str(today_month) +\
    #         ", " + str(today_day)

    parser = argparse.ArgumentParser(description='Accept a gregorian date.')
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

    jdn1 = JulianDayNumber("en")
    jdn1.set_ymd(args.year, args.month, args.day)
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
    print "Date is: " + daynames[day_of_week] + ", " +\
            str(jdn1.get_day()) + " " +\
            jdn1.get_monthname() + " " +\
            str(jdn1.get_year())
    print str(jdn1.get_jdn())

if __name__ == '__main__':
    main()
