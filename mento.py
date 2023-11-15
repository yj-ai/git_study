
def str_cal(s):
    arr = []
    
    for a in s:
        if a=='*' or a=='/':
            arr.append(a)
            s.remove(a)
    
    for b in s:
        arr.append(b)
    
    return arr