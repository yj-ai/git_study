
def str_cal(s):
    arr1 = []
    arr2 = []
    
    for a in s:
        if a=='*' or a=='/':
            arr1.append(a)
        elif a=='+' or a=='-':
            arr2.append(a)
    
    return arr1+arr2
