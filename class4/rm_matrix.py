import random
import time
import matplotlib.pyplot as plt

def create_mat(m,n):
    mat=[]
    for i in range(m):
        for j in range(n):
            mat.append(random.random())
    return mat

def mul_mat(a,b,m,n,p):
    c=[]
    for i in range(m*p):
        c.append(0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i*p+j]+=a[i*n+k]*b[k*p+j]
    return c

def benchmark(n):
    times=[]
    total=0
    dim=[]
    flops=[]
    for i in range(1,n,50):
        a=create_mat(i,i)
        b=create_mat(i,i)
        
        start=time.time()
        c = mul_mat(a,b,i,i,i)
        end=time.time()
        total+=end-start

        tflops=2*i**3/total


        times.append(end-start)
        dim.append(i)
        flops.append(tflops)
    
    plt.plot(dim,flops)
    plt.show()
    plt.plot(dim,times)
    plt.show()


m = 2
n = 4
k = 2
a=create_mat(m, n)
b=create_mat(n, k)
c=mul_mat(a,b,m, n, k)
print(c)

import numpy as np
a1 = np.array(a).reshape(m, n)
b1 = np.array(b).reshape(n, k)
c1 = np.matmul(a1, b1).flatten()


benchmark(250)