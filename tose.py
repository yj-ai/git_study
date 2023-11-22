import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
num_students = 100
korean_scores = np.random.randint(0, 101, num_students)
math_scores = np.random.randint(0, 101, num_students)
science_scores = np.random.randint(0, 101, num_students)
english_scores = np.random.randint(0, 101, num_students)


x = np.arange(num_students)
y = korean_scores
z = math_scores
w = science_scores
v = english_scores


plt.figure(figsize=(10, 8))
plt.plot(x, y, c='r', alpha=0.5, label='국어 점수')
plt.plot(x, z, c='g', alpha=0.5, label='수학 점수')
plt.plot(x, w, c='b', alpha=0.5, label='과학 점수')
plt.plot(x, v, c='y', alpha=0.5, label='영어 점수')
plt.title('과목별 점수 분포')
plt.xlabel('student number')
plt.ylabel('socre')
plt.legend(loc='best')
plt.grid(True)
plt.show()
