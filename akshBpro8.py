import matplotlib.pyplot as plt
import sys
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('Line Chart')
plt.show()
categories=['A','B','C','D','E']
values=[15,8,12,10,5]
plt.bar(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar Chart')
plt.show()
  
