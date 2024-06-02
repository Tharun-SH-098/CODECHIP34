import matplotlib.pyplot as plt
data=[1,1,2,3,3,3,4,4,5,5,5,5,6,6,6,7,8,8,9,10]
plt.hist(data,bins=5,edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

labels=['Apples','Bananas','Orange','Grapes']
sizes=[30,25,20,15]
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('Pie Chart')
plt.show()
        
        
         
