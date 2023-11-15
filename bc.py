"""
정수 리스트와 문자 리스트를
매개변수로 받아 계산
"""

def calculate_def(num_list,operate_list):

    while 1:
        if len(num_list) <= 1:
            break

        a = num_list.pop(0)
        b = num_list.pop(0)
        z = operate_list.pop(0)

        if z == "+":
            result = a + b

        elif z == "-":
            result = a - b

        elif z == "*":
            result = a * b

        else:
            result = a / b

        num_list.insert(0,result)

    return num_list[0]

print(calculate_def([1,2,3],["+","-"]))

