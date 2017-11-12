""" jdn.py

Given a Gregorian date (y, m, d), report the julian day number.
Given a JDN, report the Gregorian date

"""

#
# This is a recreation of a small portion of work that Marc Donner
# did at IBM Research back in the 1970s.  The original work included
# a rich framework of calendar conversion tools that allowed the
# conversion from virtually any calendar to any other by the
# provision of a pair of conversion tools, one from the specified
# calendar to JDN and one from JDN to the calendar.
#
# The original code was written in rex (later Rexx) and then
# recreated first in C, Pascal, Perl, and Python by Marc as time
# passed.
#

#
# Roadmap
#
# 2017-11-12 [X] Parameterize by language.
#

class JulianDayNumber(object):
    """Julian Day Number class."""

    MONTH_NAMES = {}
    MONTH_NAMES['en'] = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    MONTH_NAMES['fr'] = [
        "janvier",
        "fevrier",
        "mars",
        "avril",
        "mai",
        "juin",
        "juillet",
        "aout",
        "septembre",
        "octobre",
        "novembre",
        "decembre"
    ]

    MONTH_LENGTHS = {}
    MONTH_LENGTHS['normal'] = \
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_LENGTHS['leap'] = \
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    TOTAL_LENGTHS = {}
    TOTAL_LENGTHS['normal'] = \
        [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    TOTAL_LENGTHS['leap'] = \
        [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

    def __init__(self, language='en', year_type='normal'):
        self.language = language
        self.year_type = year_type
        self.jdn = -1
        self.year = -1
        self.month = -1
        self.day = -1
        self.jdn_flag = False
        self.ymd_flag = False

    def get_month_lengths(self, year_type=None):
        """Get the month lengths."""
        return self.MONTH_LENGTHS[\
                year_type if year_type else self.year_type]

    def get_total_lengths(self, year_type=None):
        """Get the cumulative lengths of the year to a given month."""
        return self.TOTAL_LENGTHS[\
                year_type if year_type else self.year_type]

    def get_month_names(self, language=None):
        """Get the list of month names for a language."""
        return self.MONTH_NAMES[language if language else self.language]

    def get_language(self):
        """Get the default language."""
        return self.language

    def get_year_type(self):
        """Get the year type."""
        if not self.ymd_flag:
            self.calc_ymd()
        else:
            self.calc_jdn()
            self.calc_ymd()
        return self.year_type

    def set_jdn(self, jdn):
        """Set the JDN."""
        self.jdn = jdn
        self.jdn_flag = True
        self.ymd_flag = False

    def set_ymd(self, year, month, day):
        """Set the YMD."""
        self.year = year
        self.month = month
        self.day = day
        self.jdn_flag = False
        self.ymd_flag = True

    def get_jdn(self):
        """Return the Julian Day Number."""
        if not self.jdn_flag:
            self.calc_jdn()
        return self.jdn

    def get_year(self):
        """Return the year."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.year

    def get_month(self):
        """Return the month."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.month

    def get_monthname(self):
        """Return the text name of the month."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.MonthNames[self.month - 1]

    def get_day(self):
        """Return the day."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.day

    def get_day_of_week(self):
        """Return the day of week."""
        if not self.jdn_flag:
            self.calc_jdn()
        return self.jdn + 1
        # this way 0 => Sunday, 1 => Monday, ..., 6 => Sunday

    def get_ymd(self):
        """Return the year, month, day as a tuple."""
        if not self.ymd_flag:
            self.calc_ymd()
        return (self.year, self.month, self.day)

    def calc_jdn(self):
        """Return the JDN."""
        # Day 0 of JDN is 1 January 4713 BCE
        year = self.year + 4712
        year_day = 365 * year + (year / 4)

        if (year % 4) == 0:
            self.year_type = 'leap'
        else:
            self.year_type = 'normal'
        if self.year_type == 'leap':
            year_day -= 1
        month_day = self.TOTAL_LENGTHS[self.leap

        # in the British Empire and successors, 1752-09-02
        if self.jdn > 2361221:
            year = self.year - 300
            if self.month <= 2:
                year -= 1
            self.jdn = self.jdn - (((year/100) * 3) / 4) - 1
        self.jdn_flag = True

    def calc_ymd(self):
        """Calculate the year, month, and day from a JDN."""
        # 1684595 is the JDN for -100-03-03.  146097 is the number
        # of days in 400 years in the new style calendar.
        # 2361221 is the JDN for 1752-09-02, the last day of the
        # Julian (old style) calendar in Britain and its colonies.

        jdn = self.jdn
        if jdn > 2361221:
            century = ((jdn - 1684595) * 4) / 146097
            jdn = self.jdn + ((century * 3) / 4) - 2

        year_z = (jdn / 1461) * 4
        self.day = jdn % 1461

        #    0 -  365 is year 0, a leap year,   366 days long
        #  366 -  730 is year 1, a normal year, 365 days long
        #  732 - 1096 is year 2, a normal year, 365 days long
        # 1097 - 1461 is year 3, a normal year, 365 days long

        if (self.day <= 365):
            years_in_cycle = 0
        elif ((377 <= self.day) and (self.day <= 730)):
            self.day -= 366
            years_in_cycle = 1
        elif ((731 <= self.day) and (self.day <= 1095)):
            self.day -= 731
            years_in_cycle = 2
        else:
            self.day -= 1096
            years_in_cycle = 3

        year_z += years_in_cycle
        self.year = year_z - 4712

        self.year_type = 'normal'
        if years_in_cycle == 0:
            if (self.year < 1752)
                self.year_type = 'leap'
            elif: ((self.year % 100) == 0):
                if ((self.year % 4000) !- 0):
                    if self.day > self.TOTAL_LENGTHS[self.year_type][2]:
                        self.day -= 1
                else:
                    self.year_type = 'leap'
            else:
                self.year_type = 'leap'

        for self.month in range(0, 13):
            if self.day < self.TOTAL_LENGTHS[self.year_type][self.month]:
                break
        self.day -= self.TOTAL_LENGTHS[self.year_type][self.month - 01]

        self.ymd_flag = True

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

if __name__ == '__main__':
    main()
