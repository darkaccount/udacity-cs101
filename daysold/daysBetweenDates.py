# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def isLeapYear(year):
    return False

def daysInMonth(year, month):
    if isLeapYear(year) :
        if month == 2:
            return 29
    elif month == 2:
        return 28
    elif month in (1,3,5,7,8,10,12):
        return 31
    else:
        return 30

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)   
    # YOUR CODE HERE!
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    print (days)
    return days

def test():
    test_cases = [((2012, 9, 30, 2012, 12, 30), 91), 
                  ((2012, 1, 1, 2013, 1, 1), 366),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print ("Test with data:", args, "failed")
            else:
                print ("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args)  )          
test()