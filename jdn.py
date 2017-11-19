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
        self.ymd = [-1, -1, -1]
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
        self.ymd = [year, month, day]
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
        return self.ymd[0]

    def get_month(self):
        """Return the month."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.ymd[1]

    def get_monthname(self):
        """Return the text name of the month."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.MONTH_NAMES[self.ymd[1] - 1]

    def get_day(self):
        """Return the day."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.ymd[2]

    def get_day_of_week(self):
        """Return the day of week."""
        if not self.jdn_flag:
            self.calc_jdn()
        return (self.jdn + 1) % 7
        # this way 0 => Sunday, 1 => Monday, ..., 6 => Sunday

    def get_ymd(self):
        """Return the year, month, day as a tuple."""
        if not self.ymd_flag:
            self.calc_ymd()
        return self.ymd

    def calc_jdn(self):
        """Calculate the JDN from year, month, and day."""
        # Day 0 of JDN is 1 January 4713 BCE
        year = self.ymd[0] + 4712
        year_day = 365 * year + (year / 4)

        if (year % 4) == 0:
            self.year_type = 'leap'
        else:
            self.year_type = 'normal'
        if self.year_type == 'leap':
            year_day -= 1
        month_day = self.TOTAL_LENGTHS[self.year_type][self.ymd[1] - 1]

        self.jdn = year_day + month_day + self.ymd[2]

        # in the British Empire and successors, after 1752-09-02
        if self.jdn > 2361221:
            self.jdn -= 1
            year = self.ymd[0] - 300
            if self.ymd[1] <= 2:
                year -= 1
            self.jdn -= (((year/100) * 3) / 4)

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

        year_accumulator = (jdn / 1461) * 4
        self.ymd[2] = jdn % 1461

        #    0 -  365 is year 0, a leap year,   366 days long
        #  366 -  730 is year 1, a normal year, 365 days long
        #  732 - 1096 is year 2, a normal year, 365 days long
        # 1097 - 1461 is year 3, a normal year, 365 days long

        if self.ymd[2] <= 365:
            years_in_cycle = 0
        elif (self.ymd[2] >= 366) and (self.ymd[2] < 731):
            self.ymd[2] -= 366
            years_in_cycle = 1
        elif (self.ymd[2] >= 731) and (self.ymd[2] < 1096):
            self.ymd[2] -= 731
            years_in_cycle = 2
        else:
            self.ymd[2] -= 1096
            years_in_cycle = 3

        year_accumulator += years_in_cycle
        self.ymd[0] = year_accumulator - 4712

        self.year_type = 'normal'
        if years_in_cycle == 0:
            if self.ymd[0] < 1752:
                # Pre-1752: Julian Calendar: every %4==0 is leap
                self.year_type = 'leap'
            elif (self.ymd[0] % 100) == 0:
                if (self.ymd[0] % 400) != 0:
                # Century not divisible by 400 is normal year
                # [Double exception]
                    if self.ymd[2] > self.TOTAL_LENGTHS[self.year_type][2]:
                        self.ymd[2] -= 1
                else:
                    # Century divisible by 400 is leap year
                    # [Triple exception]
                    self.year_type = 'leap'
            else:
                # Leap year (divisible by 4 but not century exception)
                # [Single exception]
                self.year_type = 'leap'

        def f(x): return \
                self.ymd[2] < self.TOTAL_LENGTHS[self.year_type][x]
        self.ymd[1] = filter(f, range(0, 13))[0]
#       for self.ymd[1] in range(0, 13):
#           if self.ymd[2] < \
#                   self.TOTAL_LENGTHS[self.year_type][self.ymd[1]]:
#               break
        self.ymd[2] -= self.TOTAL_LENGTHS[self.year_type][self.ymd[1] - 1]
        self.ymd[2] += 1

        self.ymd_flag = True

def main():
    """Main body."""



if __name__ == '__main__':
    main()
