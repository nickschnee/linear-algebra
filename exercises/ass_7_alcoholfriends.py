import numpy as np
import scipy.linalg as la
from scipy.optimize import minimize

# Blood alcohol of the three friends
Anton = 6.08
Beat = 5.4
Claus = 7.94

# Anton: 
# a Cointroic
# b Tequila Sunrise

# Beat:
# c Tequila Sunrise
# d Sidecar

# Claus:
# f City Lights
# g Sidecar
# h Hot Chili Sunshine

# Cointronic: 4cl gin, 1cl orange liqueur, 20cl tonic water
# Tequila Sunrise: 6cl tequila, 2 limes, 2cl grenadine, 10cl oj, crushed ice
# City lights: 6 cl vodka, 3 cl raspberry sirup, 250 ml mango juice, 5 ice cubes, 1 orange slice
# Sidecar: 2 cl brandy, 2 cl orange liqueur, 2 cl lemon juice
# Hot Chili Sunshine: 2 cl brandy, 2 cl peach liqueur, 1 cl lemon juice, 1 cl lime juice, 15 cl mango juice 15 cl maracuja juice, 2 chili pieces, 1 cl vodka

# Alcohol percentages of liquors
brandy = 0.38
peachliq = 0.21
vodka = 0.4
orangeliq = 0.4
gin = 0.375
tequila = 0.38
martini = 0.15


cointronic = 4 * gin + 1 * orangeliq
teqSunrise = 6 * tequila
cityLights = 6 * vodka
sidecar = 2 * brandy + 2 * orangeliq
hotChili = 2 * brandy + 2 * peachliq



# A_u = np.array([ [1.9, 2.28, 0, 0, 0, 0, 0], [0, 0, 2.28, 1.56, 0, 0, 0], [0, 0, 0, 0, 2.4, 1.56, 1.58]]) 
# b_u = np.array([ [6.08], [5.4], [7.94]])


A_u = np.array([ [1.5, 2.4, 0, 0, 0, 0, 0], [0, 0, 2.4, 2.02, 0, 0, 0], [0, 0, 0, 0, 1.9, 2.02, 1.94]]) 
b_u = np.array([ [7.8], [8.84], [9.82]])


import numpy as np
import scipy.linalg as la

#Nr.1
A = np.array([ [1.5, 2.4, 0, 0, 0, 0, 0], [0, 0, 2.4, 2.02, 0, 0, 0], [0, 0, 0, 0, 1.9, 2.02, 1.94]]) 
b = np.array([ [7.8], [8.84], [9.82]])

x_p = la.lstsq(A,b)[0]
print(x_p)

x_h = la.null_space(A)
print(x_h)

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(np.hstack([A,b])))



# rkA_u = np.linalg.matrix_rank(A_u) 
# Ab_u = np.hstack([A_u,b_u]) 
# rkAb_u = np.linalg.matrix_rank(Ab_u)

# # least squares method for xp - as we know system is consistent 
# x_p = la.lstsq(A_u,b_u)[0]

# # get xh with null_space 
# # # may contain multiple vector for each free parameter (2 in this case) 
# x_h = la.null_space(A_u)

# print(x_p) 
# print()
# print(x_h)