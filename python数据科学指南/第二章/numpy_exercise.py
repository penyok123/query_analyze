# -*- coding:utf-8 -*-
import numpy as np


def display_sahpe(a):
    print('*' * 10)
    print(a)
    print("size:%d" % a.size)
    print("ndim:%d" % a.ndim)
    print("shape", a.shape)
    print("*" * 10)


a_list = [1, 2, 3]
an_array = np.array(a_list, dtype=float)
print(an_array)
display_sahpe(an_array)

a_listoflist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a_matrix = np.matrix(a_listoflist, dtype=float)
print(a_matrix)

display_sahpe(a_matrix)
gegeral_random_numbers = np.random.randint(1, 100, size=10)

identity_matrix = np.eye(N=3, k=1)
print(identity_matrix)
display_sahpe(identity_matrix)

ones_matrix = np.ones((3, 3))
print(ones_matrix)

a_matrix = np.arange(9).reshape(3, 3)
print(a_matrix)

back_to_array = a_matrix.reshape(-1)
display_sahpe(back_to_array)

print("*" * 10)
c_max = a_matrix + a_matrix

print(c_max)

d_max = a_matrix * c_max
print(d_max)

print("*" * 10)
print(a_matrix)
e_max = np.dot(a_matrix, a_matrix)
print(e_max)
print(e_max.T)

print("*" * 100)
uniform_rnd_numbers = np.random.normal(loc=0.2, scale=0.2, size=(3, 3))
print(uniform_rnd_numbers)
