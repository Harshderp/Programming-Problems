def next_Day(y,m,d):
    '''This function will return next day(for example if you enter 2012,1,1 output will be 2012,1,2 i.e the next day)'''
    if d < daysinmonth(y,m):
        return y,m,d+1
    else:
        if m<12:
            return y,m+1,1
        else:
            return y+1,1,1
            
def dateIsbefore(y1,m1,d1,y2,m2,d2):
    '''This function will chech if the date (y1,m1,d1) is before (y2,m2,d2) '''
    if y1<y2:
        return True
    elif y1==y2:
        if m1<m2:
            return True
        if m1==m2:
            if d1<d2:
                return True
    else:
        return False

def daysinmonth(y,m):
    '''This function will return the number of days in a month'''
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    else:
        if m==2:
            if isLeapYear(y) == True:
                return 29
            return 28
        else:
            return 30

def isLeapyear(y):
    '''this function will return if a year is leap year or not'''
    if y%4==0:
        return True
    if y%100==0:
        return True
    if y%400 == 0:
        return True
    return False

def daybdates(y1,m1,d1,y2,m2,d2):
    '''This is the main function of our program as it returns the number of days between two dates'''
    days = 0
    assert not dateIsbefore(y2,m2,d2,y1,m1,d1)
    while dateIsbefore(y1,m1,d1,y2,m2,d2):
        y1,m1,d1 = next_Day(y1,m1,d1)
        days = days+1
    return days

def test():
    '''This is a function to test various test cases'''
    assert next_Day(2012,12,31) == (2013,1,1)
    assert next_Day(2013,1,31) == (2013,2,1)
    assert next_Day(2014,4,2) == (2014,4,3)
    assert dateIsbefore(2012,1,1,2013,1,1) == True
    assert dateIsbefore(2012,1,1,2011,1,1) == False
    assert dateIsbefore(2011,1,29,2011,1,31) == True
    assert daysinmonth(2012,2) == 29
    assert daysinmonth(2013,2) == 28
    assert daysinmonth(2011,1) == 31
    assert isLeapyear(2012) == True
    assert isLeapyear(2013) == False
    assert isLeapyear(2014) == False
    assert daybdates(2012,1,1,2013,1,1) == 366
    assert daybdates(2012,1,1,2012,2,1) == 31
    assert daybdates(2013,1,1,2014,1,1) == 365
    print('All test cases passed')
    
test()
