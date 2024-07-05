import random
import time
import matplotlib.pyplot as plt

def create_mat(m,n):
    mat=[]
    for i in range(m):
        for j in range(n):
            mat.append(random.randint(1,4))
    return mat

def mul_mat(a,b,m,n,p,bm,bn):
    c=[]
    for i in range(m*p):
        c.append(0)

    for batch in range(0,m,bm):
        for batch2 in range(0,n,bn):   
            for i in range(batch, min(batch+bm, m)):
                for j in range(p):
                    for k in range(batch2,min(batch2+bn,n)):
                        c[i*p+j] += a[i*n+k] * b[k*p+j]
            #print(c)  
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

m = 6
n = 12
k = 6
m_step = 3
n_step = 3

a=create_mat(m, n)
b=create_mat(n, k)
c=mul_mat(a,b,m,n,k,m_step,n_step)

import numpy as np
a1 = np.array(a).reshape(m, n)
b1 = np.array(b).reshape(n, k)
c1 = np.matmul(a1, b1).flatten()
assert np.allclose(c, c1)
