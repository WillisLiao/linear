from scipy import optimize
import numpy as np
A=0
B=0
C=0
D=0
find = np.array([-1,-1,-1,-1])
f_le = np.array([A, B, C, D])                    #le (less than and equal too)
v_le = np.array([150, 150, 150, 150])     
f_e = None
v_e = None
result = optimize.linprog(find, A_ub = f_le, b_ub = v_le, method = 'revised simplex')
while True:
    A+=1
    if 20*A+40*B+50*C+100*D <= 150:
        print(A, B, C, D)
    else:
        break
    while True:
        B+=1
        if 20*A+40*B+50*C+100*D <= 150:
            print(A, B, C, D)
        else:
            break
        while True:
            C+=1
            if 20*A+40*B+50*C+100*D <= 150:
                print(A, B, C, D)
            else:
                break
            while True:
                D+=1
                if 20*A+40*B+50*C+100*D <= 150:
                    print(A, B, C, D)
                else:
                    break
            
        
    