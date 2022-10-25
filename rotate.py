# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import numpy as np
import math


def x_rot(ori, q_in):
    ang = -q_in
    x_mat = [[1, 0, 0],
             [0, math.cos(ang), -math.sin(ang)],
             [0, math.sin(ang), math.cos(ang)]]
    return np.dot(ori, x_mat)


def y_rot(ori, q_in):
    ang = -q_in
    y_mat = [[math.cos(ang), 0, math.sin(ang)],
             [0, 1, 0],
             [-math.sin(ang), 0, math.cos(ang)]]
    return np.dot(ori, y_mat)


def z_rot(ori, q_in):
    ang = -q_in
    z_mat = [[math.cos(ang), -math.sin(ang), 0],
             [math.sin(ang), math.cos(ang), 0],
             [0, 0, 1]]
    return np.dot(ori, z_mat)