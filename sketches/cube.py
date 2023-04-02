
from rhinestone import *
import numpy as np
from math import sin, cos, radians

svg = SVG("cube")

points = [
    np.array([-0.5, -0.5, -0.5]),
    np.array([ 0.5, -0.5, -0.5]),
    np.array([ 0.5,  0.5, -0.5]),
    np.array([-0.5,  0.5, -0.5])]

theta = radians(30)

z_mat = np.array([
    [cos(theta), -sin(theta), 0],
    [sin(theta),  cos(theta), 0],
    [0,          0,           1]])

y_mat = np.array([
        [cos(theta), 0, sin(theta)],
        [0, 1, 0],
        [-sin(theta), 0, cos(theta)],
    ])

x_mat = np.array([
    [1, 0, 0],
    [0, cos(theta), -sin(theta)],
    [0, sin(theta), cos(theta)],
])

p_mat = np.array([
    [1, 0, 0],
    [0, 1, 0],
])

p = []

for i in points:
    r = np.dot(z_mat, i)
    r = np.dot(y_mat, r)
    r = np.dot(x_mat, r)
    p.append(np.dot(p_mat, r))

svg.add_points([i * 0.5 + 0.5 for i in p], stroke_color="pink")

print(p)
                       
#    [[-0.5, -0.5,  0.5], 
#     [ 0.5, -0.5,  0.5], 
#     [ 0.5,  0.5,  0.5], 
#     [-0.5,  0.5,  0.5]], 
#                       
#    [[-0.5,  0.5,  0.5], 
#     [-0.5,  0.5, -0.5], 
#     [-0.5, -0.5, -0.5], 
#     [-0.5, -0.5,  0.5]], 
#    
#    [[ 0.5,  0.5,  0.5], 
#     [ 0.5,  0.5, -0.5], 
#     [ 0.5, -0.5, -0.5], 
#     [ 0.5, -0.5,  0.5]], 
#                       
#    [[-0.5, -0.5, -0.5], 
#     [ 0.5, -0.5, -0.5], 
#     [ 0.5, -0.5,  0.5], 
#     [-0.5, -0.5,  0.5]], 
#                       
#    [[-0.5,  0.5, -0.5], 
#     [ 0.5,  0.5, -0.5], 
#     [ 0.5,  0.5,  0.5], 
#     [-0.5,  0.5,  0.5]] 
#]



svg.save()

