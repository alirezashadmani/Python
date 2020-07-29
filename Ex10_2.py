import numpy as np
import matplotlib.pyplot as plt
vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]]
vec2 = (np.pi/4) * vec1
vec2 = np.cos( vec2 )
vec3 = vec1 + 2 * vec2
vec4 = np.multiply(mat1, vec3)
Tmat1 = mat1.transpose()
DTmat1 = np.linalg.det(mat1)
TRmat1 = np.trace(mat1)
Minvec1 = np.min(vec1)
jvalue = np.where(vec1 === np.min(vec1))
print(jvalue)
Minmat1 = np.min(mat1)

A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])

sumrow = np.sum(A,axis=1)
sumco1 = np.sum(A,axis = 0)
sumdia = np.sum(np.dia(A))
sumflip = np.sum(np.fliplr(A))

if np.min(np.sum(A,axis=1)) == np.max(np.sum(A,axis=1)) == np.min(np.sum(A,axis=0)) == np.max(np.sum(A,axis=0)) == np.sum(A.diagonal()):
                print('Magic Matrix')
