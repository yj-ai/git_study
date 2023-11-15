
def str_cal(s):
    arr1 = []
    arr2 = []
    
    for a in s:
        if a=='*' or a=='/':
            arr1.append(a)
        else:
            arr2.append(a)
    
    return arr1+arr2
