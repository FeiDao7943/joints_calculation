import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings("ignore")


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


def cor_calculate(num, points_dic, length_dic, lth, q_x, q_y, q_z):
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
    aft_yrot = y_rot(new_cor, q_y)
    new_cor = aft_yrot
    aft_zrot = z_rot(new_cor, q_z)
    new_cor = aft_zrot

    points_dic[num + 1, :] = new_cor + points_dic[num]
    return points_dic


def draw_fig(points_dic):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlim3d(0, 6)
    ax.set_ylim3d(0, 6)
    ax.set_zlim3d(0, 6)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(points_dic[:, 0], points_dic[:, 1], points_dic[:, 2], 'bo--')
    ax.plot(points_dic[0, 0], points_dic[0, 1], points_dic[0, 2], 'ro')
    plt.show()


def main(joint_num):
    total_joint = joint_num
    # initialized setting
    points_list = np.zeros((total_joint + 2, 3))
    length_list = np.zeros(total_joint + 1)
    origin = [0, 0, 0]
    points_list[0, :] = origin
    tiny = 10e-8
    pi = np.pi
    # plug a joint with tiny length as the joint 0
    pot_0 = [0, 0, tiny]  # has a direction goes up the z axis
    points_list[1, :] = pot_0
    length_list[0] = tiny

    '''
    joint example ---
    q(i)_x = rotation angle respect to x-axis
    q(i)_y = rotation angle respect to y-axis
    q(i)_z = rotation angle respect to z-axis
    l(i) = length of the link
    '''

    # joint 1 ---------
    q1_x = pi * 0
    q1_y = pi * 1/4
    q1_z = pi * 1/3
    l1 = 1

    # joint 2 ---------
    q2_x = pi * 1/3
    q2_y = pi * 1/6
    q2_z = pi * 1/8
    l2 = 2

    # joint 3 ---------
    q3_x = pi * 1/4
    q3_y = pi * 1/4
    q3_z = pi * 1/6
    l3 = 3

    # calculating part
    points_list = cor_calculate(1, points_list, length_list, l1, q1_x, q1_y, q1_z)
    points_list = cor_calculate(2, points_list, length_list, l2, q2_x, q2_y, q2_z)
    points_list = cor_calculate(3, points_list, length_list, l3, q3_x, q3_y, q3_z)

    # print part
    print('origin  : ', end='')
    print('[%.2f, %.2f, %.2f]' % (origin[0], origin[1], origin[2]))
    for i in range(total_joint):
        print('joint', str(i), ': ', end='')
        print('[%.2f, %.2f, %.2f]' % (points_list[i+2][0], points_list[i+2][1], points_list[i+2][2]))

    draw_fig(points_list)


if __name__ == '__main__':
    # variable of main() is the number of joints
    main(3)
