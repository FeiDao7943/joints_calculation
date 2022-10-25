# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
from drawer import draw_fig, print_part
from rotate import x_rot, y_rot, z_rot
from joint_posi import cor_calculate, distance_cal
import warnings
warnings.filterwarnings("ignore")


parser = argparse.ArgumentParser()
parser.add_argument('--joint_num', type=int, default=0, help='number of joints')
# parser.add_argument('--max_epoch', type=int, default=180, help='Epoch to run [default: 180]')
FLAGS = parser.parse_args()


def initialized(joint_num):
    total_joint = joint_num
    # initialized setting
    axis = [[0, 0, 0], [0.5, 0, 0], [-0.1, 0, 0],
            [0, 0, 0], [0, 0.5, 0], [0, -0.1, 0],
            [0, 0, 0], [0, 0, 0.5], [0, 0, -0.1]]
    axis = np.asarray(axis)
    axis_list = np.zeros((joint_num + 1, 9, 3))
    axis_list[0, :, :] = axis
    points_list = np.zeros((total_joint + 2, 3))
    length_list = np.zeros(total_joint + 1)
    origin = [0, 0, 0]
    points_list[0, :] = origin
    tiny = 10e-8
    pi = np.pi
    # plug a joint with tiny length as the joint 0
    pot_0 = [tiny, 0, 0]  # has a direction goes up the z axis
    points_list[1, :] = pot_0
    length_list[0] = tiny
    return points_list, length_list, axis_list


def main_processor(joint_num):
    points_list, length_list, axis_list = initialized(joint_num)

    pi = np.pi

    '''
    joint example ---
    q(i)_x = rotation angle respect to x-axis
    q(i)_y = rotation angle respect to y-axis
    q(i)_z = rotation angle respect to z-axis
    l(i) = length of the link
    '''
    # target coordinate
    target = [3, 3, 3]
    error_ignored = 0.01

    # joint 1 ---------
    q1_x = pi * 0
    q1_y = pi * -1 / 3
    q1_z = pi * 1 / 6
    l1 = 2

    # joint 2 ---------
    q2_x = pi * 0
    q2_y = pi * 1 / 6
    q2_z = pi * 1 / 8
    l2 = 2

    # joint 3 ---------
    q3_x = pi * 0
    q3_y = pi * 1 / 6
    q3_z = pi * -1 / 6
    l3 = 2

    # conclusion
    length_dic = np.zeros(joint_num)
    angle_dic = np.zeros((joint_num, 3))
    for counter in range(joint_num):
        length_dic[counter] = int(locals()['l' + str(counter+1)])
        angle_dic[counter][0] = float(locals()['q' + str(counter + 1) + '_x'])
        angle_dic[counter][1] = float(locals()['q' + str(counter + 1) + '_y'])
        angle_dic[counter][2] = float(locals()['q' + str(counter + 1) + '_z'])

    # result finding
    max_length = sum(length_dic)
    target_dis = distance_cal([0, 0, 0], target)
    if target_dis > max_length:
        print('Length not enough')
        exit()

    # calculating part
    points_list, axis_list = cor_calculate(1, points_list, length_list, axis_list, l1, q1_x, q1_y, q1_z)
    points_list, axis_list = cor_calculate(2, points_list, length_list, axis_list, l2, q2_x, q2_y, q2_z)
    points_list, axis_list = cor_calculate(3, points_list, length_list, axis_list, l3, q3_x, q3_y, q3_z)

    # print_part([0, 0, 0], points_list)
    # draw_fig(3, points_list, axis_list, 'joint')


if __name__ == '__main__':
    # variable of main() is the number of joints
    main_processor(FLAGS.joint_num)



