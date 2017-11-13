""" test-jdn.py

Run some tests on the jdn.py class.

"""

from jdn import JulianDayNumber

def main():
    """Main body."""

    jdn1 = JulianDayNumber("en")
    jdn2 = JulianDayNumber("fr", "leap")

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

    print "YMD to JDN test"
    print "2017-11-12"
    jdn1.set_ymd(2017, 11, 12)
    print jdn1.get_jdn()

    print "2017-11-13"
    jdn1.set_ymd(2017, 11, 13)
    print jdn1.get_jdn()

    print "1752-09-01"
    jdn1.set_ymd(1752, 9, 1)
    print jdn1.get_jdn()

    print "1752-09-02"
    jdn1.set_ymd(1752, 9, 2)
    print jdn1.get_jdn()

    print "1752-09-13"
    jdn1.set_ymd(1752, 9, 14)
    print jdn1.get_jdn()

    print "1752-09-14"
    jdn1.set_ymd(1752, 9, 15)
    print jdn1.get_jdn()

if __name__ == '__main__':
    main()