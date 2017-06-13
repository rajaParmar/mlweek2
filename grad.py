import numpy as np
import matplotlib.pyplot as plt
import math
import numpy

def cost(x,y,theta):
	temp=0
	for i in range(0,x.shape[0]-1):
		temp=temp+(hypothesis(theta,x[i])-y[i])**2
	temp=temp/(2*x.shape[0])
	return temp

def hypothesis(theta,x):
	return theta[0]+theta[1]*x

def plot_final(x,y,theta):
	plt.plot(data[:,0],data[:,1],'r+')
	plt.plot(x,eval('theta[0]+theta[1]*x'))
	plt.show()	

def update(theta,x,y,alpha):
	temp=0
	temp2=0
	for i in range(0,x.shape[0]-1):
		temp=temp+((hypothesis(theta,x[i])-y[i]))
		temp2=temp2+((hypothesis(theta,x[i])-y[i])*x[i])
	# print(temp)
	# print(temp2)
	theta[0]=theta[0]-(alpha/x.shape[0])*temp
	theta[1]=theta[1]-(alpha/x.shape[0])*temp2
	#print(theta)

filename="ex1data1.txt"
raw=open(filename,'rt')
data=np.loadtxt(raw,delimiter=",")
theta=np.array([0,0],dtype=np.float)
x=data[:,0]
y=data[:,1]

x=x[1:]
y=y[1:]

print(cost(x,y,theta))

print(theta)
#plot_final(x,y,theta)
cost_plt=[]
itr=[]
iterations=10000


for i in range(0,iterations):
	update(theta,x,y,0.01)
	cost_plt.append(cost(x,y,theta))
	#theta_plot.append(theta[1])
	#print(cost(x,y,theta))
	itr.append(i)



# print(theta)
print(cost(x,y,theta))
plot_final(x,y,theta)

#print(cost_plt)
plt.plot(np.array(itr),np.array(cost_plt))
# #plt.plot(theta_plot,cost_plt,'b')
plt.xlabel('iterations')
plt.ylabel('Cost')
plt.show()











