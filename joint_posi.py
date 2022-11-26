# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import numpy as np
import math
from rotate import x_rot, y_rot, z_rot


def cor_calculate(num, points_dic, length_dic, axis_draw, lth, q_x, q_y, q_z):
    '''
    :param num: serial number of joints
    :param points_dic: dictionary stored all coordinates of joints
    :param length_dic: dictionary stored all length of links
    :param lth: length of temporary joint
    :param q_x: rotation angle of x_axis
    :param q_y: rotation angle of y_axis
    :param q_z: rotation angle of z_axis
    :return: dictionary stored all coordinates of joints
    '''
    length_dic[num] = lth
    dir_vet = points_dic[num] - points_dic[num - 1]
    new_cor = np.dot(dir_vet, length_dic[num] / length_dic[num - 1])

    aft_xrot = x_rot(new_cor, q_x)
    new_cor = aft_xrot
    aft_yrot = y_rot(new_cor, -q_y)
    new_cor = aft_yrot
    aft_zrot = z_rot(new_cor, q_z)
    new_cor = aft_zrot
    points_dic[num + 1, :] = new_cor + points_dic[num]

    new_axis_draw = np.zeros((9, 3))
    for i in range(9):
        new_cor_axis = axis_draw[num-1, i, :] - points_dic[num, :]
        aft_xrot = x_rot(new_cor_axis, q_x)
        new_cor_axis = aft_xrot
        aft_yrot = y_rot(new_cor_axis, -q_y)
        new_cor_axis = aft_yrot
        aft_zrot = z_rot(new_cor_axis, q_z)
        new_cor_axis = aft_zrot
        new_axis_draw[i, :] = new_cor_axis + points_dic[num+1, :]
    axis_draw[num, :, :] = new_axis_draw
    return points_dic, axis_draw


def distance_cal(coor1, coor2):
    x_2 = pow(coor1[0] - coor2[0], 2)
    y_2 = pow(coor1[1] - coor2[1], 2)
    z_2 = pow(coor1[2] - coor2[2], 2)
    dis = pow(x_2 + y_2 + z_2, 0.5)
    return dis
