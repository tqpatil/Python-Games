import numpy as np
import matplotlib.pyplot as plt
import random
x=[]
y=[]
dice=[1,2,3,4,5,6]
for i in range(1,100):
    x.append(i)
for i in range(1,100):
    y.append(random.choice(dice)+random.choice(dice))








fig = plt.figure(tight_layout=True)

ax = fig.add_subplot(2, 2, 1) # using a different approach to arrange plots
ax.scatter(x, y, s=2, color='green')
ax.set_title("Scatter")
ax.set_xlabel('x')
ax.set_ylabel('y')

ax = fig.add_subplot(2, 2, 2)
ax.plot(x,y)
ax.set_title("Line")
ax.set_xlabel('x')
ax.set_ylabel('y')  

ax = fig.add_subplot(2, 2, 3)
ax.set_title("Pie Plot")
dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for i in range(len(y)):
    dict[y[i]]+=1
major = list(dict.keys())
students = list(dict.values())
ax.pie(students, labels = major,autopct='%1.0f%%')

ax = fig.add_subplot(2, 2, 4)
ax.set_title("Histogram")
ax.hist(y,bins=11)
plt.show()