""" testjdn.py

Run some tests on the jdn.py class.

"""

from jdn import JulianDayNumber
# import psutil
import time

def iso8601_from_ymd(year, month, day):
    """Format three integers into an ISO8601 string."""
    display_year = ('0000' + str(year))[-4:]
    display_month = ('00' + str(month))[-2:]
    display_day = ('00' + str(day))[-2:]
    return display_year + "-" + display_month + "-" + display_day

def main():
    """Main body."""

    # capture timing information
    # cputime_0 = psutil.cpu_times()
    cputime_0 = time.time()

    jdn1 = JulianDayNumber("en")
    jdn2 = JulianDayNumber("fr", "leap")

    test_plan = [
        {'jdn':2458070, 'ymd':(2017, 11, 12)},
        {'jdn':2458071, 'ymd':(2017, 11, 13)},
        {'jdn':2361220, 'ymd':(1752, 9, 1)},
        {'jdn':2361221, 'ymd':(1752, 9, 2)},
        {'jdn':2361222, 'ymd':(1752, 9, 14)},
        {'jdn':2361223, 'ymd':(1752, 9, 15)}
    ]

    print "jdn1"
    print "Language: " + jdn1.get_language()
    print "Year type: " + jdn1.get_year_type()
    print "Month lengths: " + \
            str(jdn1.get_month_lengths())
    print "Total lengths: " + \
            str(jdn1.get_total_lengths())
    print "Month names: " + \
            str(jdn1.get_month_names())

    print

    print "jdn2"
    print "Language: " + jdn2.get_language()
    print "Year type: " + jdn2.get_year_type()
    print "Month lengths: " + \
            str(jdn2.get_month_lengths())
    print "Total lengths: " + \
            str(jdn2.get_total_lengths())
    print "Month names: " + \
            str(jdn2.get_month_names())

    print "\nYMD to JDN test"
    for test in range(0, len(test_plan)):
        jdn = test_plan[test]["jdn"]
        [year, month, day] = test_plan[test]["ymd"]
        print iso8601_from_ymd(year, month, day) + " => " + str(jdn)
        jdn1.set_ymd(year, month, day)
        print str(jdn1.get_jdn())
        print

    print "JDN to YMD test"
    for test in range(0, len(test_plan)):
        jdn = test_plan[test]["jdn"]
        [year, month, day] = test_plan[test]["ymd"]
        print str(jdn) + " => " + iso8601_from_ymd(year, month, day)
        jdn2.set_jdn(jdn)
        [year, month, day] = jdn2.get_ymd()
        print iso8601_from_ymd(year, month, day)
        print

    print "now to test 9999647 dates"

    day_histogram = {}
    for day in range(1, 32):
        day_histogram[day] = 0

    month_histogram = {}
    for month in range(1, 13):
        month_histogram[month] = 0

    for jdn_probe in range(0, 9999647):
        jdn1.set_jdn(jdn_probe)
        [year, month, day] = jdn1.get_ymd()
        jdn2.set_ymd(year, month, day)
        jdn_check = jdn2.get_jdn()
        month_histogram[month] += 1
        day_histogram[day] += 1
        if jdn_probe != jdn_check:
            print "Error: probe: " + str(jdn_probe) + \
                    " check: " + str(jdn_check) + " => " + \
                    str(jdn_probe - jdn_check) + \
                    " (" + iso8601_from_ymd(year, month, day) + ")"

    print "\nDay breakdown:"
    for day in day_histogram:
        print str(day) + ": " + str(day_histogram[day])

    print "\nMonth breakdown:"
    for month in month_histogram:
        print str(month) + ": " + str(month_histogram[month])

    # cputime_1 = psutil.cpu_times()
    cputime_1 = time.time()
    print
    # index 0 is user
    # index 1 is nice
    # index 2 is system
    # index 3 is idle
    print "Elapesed time: " + str(cputime_1 - cputime_0)
    # print "User time: " + str(cputime_1[0] - cputime_0[0])
    # print "System time: " + str(cputime_1[2] - cputime_0[2])

if __name__ == '__main__':
    main()
