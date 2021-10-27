from scipy import optimize
import numpy as np

find = np.array([-1,-1,-1,-1])
f_le = np.array([20, 40, 50, 100])                    #le (less than and equal too)
v_le = np.array([150, 150, 150, 150])     
f_e = None
v_e = None
result = optimize.linprog(find, A_ub = f_le, b_ub = v_le, method = 'revised simplex')
