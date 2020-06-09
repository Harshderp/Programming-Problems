def bigger(a,b):
    '''to find bigger number from two numbers'''
    if a>b:
        return a
    return b

def biggest(a,b,c):
    '''To find biggest number from three numbers'''
    return bigger(a,bigger(b,c))

def median(a,b,c):
    '''To find the median of three numbers using the functions above'''
    big = biggest(a,b,c)
    if big==a:
        return bigger(b,c)
    elif big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)
    
def test():
    '''This function will check if all the test case are pass or not'''
    assert median(1,2,3) == 2
    assert median(1,2,1) == 1
    assert median(2,4,1) == 2
    assert median(1,1,2) == 1
    assert median(3,7,9) == 7
    assert median(1,1,1) == 1
    print('All test cases passed')
test()
        
