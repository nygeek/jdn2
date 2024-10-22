# JDN2

Julian Day Number calculations

This is a residual implemntation of the jdn functions written in Python2.

It is not being maintained, so if you want the maintained version go to
https://github.com/nygeek/jdn ...

This code started life as a rex (later REXX) program at IBM in the
late 1970s.  When I left IBM to go to grad school, I reimplemented it
in C.  Subsequently I reimplemented it in Perl and then in Python2.
Some of the style oddities in the Python2 implementation are residues
of some C-isms that I carried along.  The Python3 implementation
eliminates the weirdness that came from the C - Perl - Python2 porting.
It also eliminates the initial i18n work that can be seen in this
implementation.

There is a test program (test2.py) that validates the calc_jdn() and
calc_ymd() functions.  Here is the concept behind this test plan:

1 - the composition calc_jdn(calc_ymd(j)) should be j for all j.

2 - there is a set of histograms of the value of m and d from
    (y, m, d) for j in the range from 0 to 9999647.  The reference
    histograms are the result of a set of first-principles calculations.

## background

***calc_jdn( year, month, day )*** computes the Julian Day Number (JDN).

This is a measure of time that starts on 1 January 4713 BCE and
increments uniformly.  It is used extensively by astronomers because
of its uniformity.  This system deviates from the classical JDN,
which changes at noon rather than at midnight.  This begs the
question of noon *where*, of course.

***calc_ymd( jdn )*** inverts the calculation in julian and returns

( year, month, day ) corresponding to the proffered jdn.  Note that
this implementation of the calculator assumes that the switch from
the old Julian calendar to the Gregorian calendar took place on 2
September 1752, which is correct by-and-large for the English-speaking
world.

In much of the rest of the world the change happened on 15 October
1582, during the papacy of Gregory the XIII, for whom the Gregorian
Calendar is named.

The Julian Day Number is based on the work of Joseph Scaliger, a
scholar who proposed it at the time of the Gregorian calendar reform.
