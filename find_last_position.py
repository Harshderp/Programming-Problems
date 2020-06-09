def find_last(s,t):
'''This function will return the last position(index) where the target substring of a string was occured'''
    last_pos = -1
    while True:
        pos = s.find(t,last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos
