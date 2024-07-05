import random
import time
import matplotlib.pyplot as plt
import numpy as np

def create_mat(m, n):
    mat = []
    for i in range(m):  
        row = []
        for j in range(n):  
            row.append(random.random())  
        mat.append(row)  
    return mat

def mul_mat(a, b):
    if len(a[0]) != len(b):
        raise Exception("Error:wrong matrix dimensions")
    else:
        c=[]
        for i in range(len(a)):
            row=[]
            for j in range(len(b[0])):
                row.append(0)
            c.append(row)
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
    return c



a=create_mat(3,3)
b=create_mat(3,3)

def benchmark(n):
    times=[]
    total=0
    dim=[]
    flops=[]
    for i in range(0,n,50):
        a=create_mat(i+1,i+1)
        b=create_mat(i+1,i+1)
        
        start=time.time()
        #c = mul_mat(a,b)
        np.matmul(a,b)
        end=time.time()
        total+=end-start

        tflops=2*i**3/total


        times.append(end-start)
        dim.append(i+1)
        flops.append(tflops)
    
    plt.plot(dim,flops)
    plt.show()
    plt.plot(dim,times)
    plt.show()


benchmark(500)
    




