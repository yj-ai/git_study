"""문자열 s를 매개변수로 입력 받아 나누어
정수리스트, 문자 리스트로 반환하는 함수
"""


def sh(s):
    li = s.split(" ")
    num_list = []
    operate_list = []

    for i in li:
        if i.isdigit():
            i = int(i)
            num_list.append(i)

        else:
            operate_list.append(i)

    return num_list, operate_list
# ss

# 예시
s = "9 + 4 * 9"

print(sh(s))

