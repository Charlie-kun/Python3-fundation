import numpy as np

def fuction2(x):
    return x[0]**2+x[1]**2

def numberiacal_gradient(f,x):
    h=1e-4    #0.0001
    grad=np.zeros_like(x)    #same shape array x

    for idx in range(x.size):
        temp_val=x[idx]    #calculate f(x+h)
        x[idx]=temp_val+h
        fxh1=f(x)

        x[idx]=temp_val-h
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=temp_val    #return orgin value.

    return grad


print(numberiacal_gradient(fuction2, np.array([3.0,4.0])))    #[6,8.]
