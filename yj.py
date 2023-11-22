import numpy as np
import matplotlib.pyplot as plt

def Scatt(number, arr1, arr2, arr3, arr4):
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    x = np.arrange(number+1)
    
    for i in range(len(arr1)):
        if arr1[i] >= 10:
            result1.append(arr1[i])
        if arr2[i] >= 10:
            result2.append(arr2[i])
        if arr3[i] >= 10:
            result3.append(arr3[i])
        if arr4[i] >= 10:
            result4.append(arr4[i])
    
    plt.scatter(x,result1, color = 'blue', label = 'Korean')
    plt.scatter(x,result2, color = 'green', label = 'Math')
    plt.scatter(x,result3, color = 'red', label = 'Science')
    plt.scatter(x,result4, color = 'black', label = 'English')
    
    plt.title('Exam Scores')
    plt.xlabel('Subjects')
    plt.ylabel('Scores')
    plt.legend()
    
    plt.show()