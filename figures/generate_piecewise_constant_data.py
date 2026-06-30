import numpy as np 

# output file name 
fname: str = "double_integral1_data.txt"
# function  
func = lambda x, y: 0.5 * np.sin(x*np.pi) * np.sin(y*np.pi) 

# domain 
N: int = 11
x = np.linspace(0, 1, N+1) 
y = np.linspace(0, 1, N+1) 
# value of function 
xmid = (x[1:]+x[:-1])/2 
ymid = (y[1:]+y[:-1])/2 
xd = np.vstack((x, x)).T.ravel()
yd = np.vstack((y, y)).T.ravel()
xx, yy = np.meshgrid(xd, yd)
xmid, ymid = np.meshgrid(xmid, ymid)
v = func(xmid, ymid).ravel()
vtemp = np.vstack((v, v)).T.reshape(-1, 2*N) 
vtemp = np.hstack((np.zeros((N, 1)), vtemp, np.zeros((N, 1))))
vv = np.hstack((vtemp, vtemp)).reshape(-1, 2*(N+1))
vv = np.vstack((np.zeros((1, 2*(N+1))), vv, np.zeros((1, 2*(N+1)))))

with open(fname, mode="w") as outfile: 
    outfile.write('# piecewise constant function \n') 
    outfile.write('x y value \n') 
    for i in range(2*(N+1)):
        np.savetxt(outfile, np.vstack((xx[i], yy[i], vv[i])).T, fmt="%.6f")
        outfile.write('\n') 

