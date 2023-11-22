import numpy as np
import matplotlib.pyplot as plt

def sh2(count):
    import numpy as np
    import random
    kor = []
    math = []
    science = []
    english = []
    for i in range(1, count + 1):
        a = int(random.randint(1, 101))
        b = int(random.randint(1, 101))
        c = int(random.randint(1, 101))
        d = int(random.randint(1, 101))
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


def hi(kor, math, science, english, sn):
    
    studentnumber = np.arange(sn)

    plt.plot(studentnumber, kor, c='r')
    plt.plot(studentnumber, math, c='b')
    plt.plot(studentnumber, science, c='g')
    plt.plot(studentnumber, english, c='y')
    plt.show()
k , m , s , e = sh2(100)
hi(k,m,s,e,100)
