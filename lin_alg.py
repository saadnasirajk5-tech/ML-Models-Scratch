# dot product 
import numpy as np 
v1 = np.array([1,2,3]) 
v2 = np.array([3,4,5]) 
dot_product = np.dot(v1,v2) 
print(dot_product)      
##################################################
# writing a polynomial with numpy  
poly_1 = np.poly1d([3,2,1]) 
print(poly_1(2)) #it plugged x=2 in polynomial 
###################################################
#Sum of two matrices 
A = np.array([
    [1,6],
    [8,4]
])
B= np.array([
    [7,9],
    [7,6]
])
C= A+B   
C=np.add(A,B) 
print(C)
#############################################################