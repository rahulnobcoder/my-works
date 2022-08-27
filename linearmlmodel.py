%matplotlib inline
import numpy as np
import pandas as p
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20.0,10.0)

data = p.read_csv('ds_salaries.csv')
data.head()
#default take x and y in caps to represent columns etc and remove this comment before copying this code to paste anywhere
an 
x=data['salary'].values
y=data['number'].values
mean_x=np.mean(x)
mean_y=np.mean(y)

m=len(x)

numer=0
denom=0
for i in range(m):
    numer = numer + (x[i]-mean_x)*(y[i]-mean_y)
    denom = denom + (x[i]-mean_x)**2
b1=numer/denom
b0=mean_y - (b1*mean_x)
print(b1,b0)
max_x = np.max(x) 
min_x = np.min(x)
a=np.linspace(min_x,min_x,len(x))
b=b0+b1*x
plt.plot(a,b,color='#58b970', label='Regression Line')
plt.scatter(x,y,c='#ef5423',label='Scatter Plot')
plt.xlabel('salary')
plt.ylabel('number')
plt.legend()
plt.show
