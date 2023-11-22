def sh2(count):
    import numpy as np
    import random

    kor = []
    math = []
    science = []
    english = []

    for i in range(1, count + 1):
        a = int(random.randint(0, 101))
        b = int(random.randint(0, 101))
        c = int(random.randint(0, 101))
        d = int(random.randint(0, 101))
        kor.append(a)
        math.append(b)
        science.append(c)
        english.append(d)
    kor = np.array(kor)
    math = np.array(math)
    science = np.array(science)
    english = np.array(english)
    return kor, math, science, english


print(sh2(1000))
