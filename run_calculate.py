import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
from drawer import draw_fig, print_part
from jacobian import velocity, jacobian_2
from rotate import x_rot, y_rot, z_rot
from torque import torque_cal
from joint_posi import cor_calculate
import warnings
warnings.filterwarnings("ignore")


parser = argparse.ArgumentParser()
parser.add_argument('--link_num', type=int, default=0, help='number of joints')
parser.add_argument('--position', action='store_true', help='calculate position')
parser.add_argument('--jacobian', action='store_true', help='calculate jacobian')
parser.add_argument('--velocity', action='store_true', help='calculate velocity')
parser.add_argument('--torque', action='store_true', help='calculate torque')

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
    pi = np.pi
    return points_list, length_list, axis_list, pi, tiny


def main_processor(joint_num):
    points_list, length_list, axis_list, pi, tiny = initialized(joint_num)

    '''
    joint example ---
    q(i)_x = rotation angle respect to x-axis
    q(i)_y = rotation angle respect to y-axis
    q(i)_z = rotation angle respect to z-axis
    l(i) = length of the link
    '''
    # joint 1 ---------
    q1_x = pi * 0
    q1_y = pi * 0
    q1_z = pi * 1 / 6

    q1_x_angu = 0
    q1_y_angu = 0
    q1_z_angu = pi * 1 / 6

    l1 = 2

    # joint 2 ---------
    q2_x = pi * 0
    q2_y = pi * 0
    q2_z = pi * 1 / 6

    q2_x_angu = 0
    q2_y_angu = 0
    q2_z_angu = pi * 1 / 6

    l2 = 2

    # joint 3 ---------
    q3_x = pi * 0
    q3_y = pi * 0
    q3_z = pi * 1 / 6

    q3_x_angu = 0
    q3_y_angu = 0
    q3_z_angu = pi * 1 / 6

    l3 = 2

    # collect part
    link_length = [l1, l2, l3]
    angle = [q1_z, q2_z, q3_z]
    angular_v = [q1_z_angu, q2_z_angu, q3_z_angu]
    # conclusion
    length_dic = np.zeros(joint_num)
    angle_dic = np.zeros((joint_num, 3))
    for counter in range(joint_num):
        length_dic[counter] = int(locals()['l' + str(counter+1)])
        angle_dic[counter][0] = float(locals()['q' + str(counter + 1) + '_x'])
        angle_dic[counter][1] = float(locals()['q' + str(counter + 1) + '_y'])
        angle_dic[counter][2] = float(locals()['q' + str(counter + 1) + '_z'])

    # calculating part
    if FLAGS.link_num == 1:
        points_list, axis_list = cor_calculate(1, points_list, length_list, axis_list, l1, q1_x, q1_y, q1_z)
    if FLAGS.link_num == 2:
        points_list, axis_list = cor_calculate(1, points_list, length_list, axis_list, l1, q1_x, q1_y, q1_z)
        points_list, axis_list = cor_calculate(2, points_list, length_list, axis_list, l2, q2_x, q2_y, q2_z)
    if FLAGS.link_num == 3:
        points_list, axis_list = cor_calculate(1, points_list, length_list, axis_list, l1, q1_x, q1_y, q1_z)
        points_list, axis_list = cor_calculate(2, points_list, length_list, axis_list, l2, q2_x, q2_y, q2_z)
        points_list, axis_list = cor_calculate(3, points_list, length_list, axis_list, l3, q3_x, q3_y, q3_z)

    print_part([0, 0, 0], points_list)

    # identify functions
    if FLAGS.position:
        x_f = (l1*math.cos(q1_z)+l2*math.cos(q1_z+q2_z)+l3*math.cos(q1_z+q2_z+q3_z))
        y_f = (l1*math.sin(q1_z)+l2*math.sin(q1_z+q2_z)+l3*math.sin(q1_z+q2_z+q3_z))
        z_f = 0
        posi_f = [x_f, y_f, z_f]
        print('position by formula', end=' ')
        print("[%.3f, %.3f, %.3f]" % (posi_f[0], posi_f[1], posi_f[2]))

    if FLAGS.jacobian:
        if FLAGS.link_num != 3:
            print('\nthis jacobian matrix design for 3 links manipulator!')
        velocity_jac = jacobian_2(link_length, angle, angular_v)
        print("final velocity by jacobian", end=' ')
        print("[%.3f, %.3f, %.3f]" % (velocity_jac[0], velocity_jac[1], 0))

    if FLAGS.velocity:
        final_velocity = velocity(link_length, angle, angular_v)
        print("final velocity by formula", end=' ')
        # print(final_velocity)
        print("[%.3f, %.3f, %.3f]" % (final_velocity[0], final_velocity[1], 0))

    if FLAGS.torque:
        torque_list = torque_cal(link_length, angle, 0, 98)
        print("torque list", end=' ')
        # print(torque_list)
        print("[%.3f, %.3f, %.3f]" % (torque_list[0], torque_list[1], torque_list[2]))

    # drawing part
    if FLAGS.velocity:
        draw_fig(3, points_list, axis_list, final_velocity, 'velocity')
    else:
        draw_fig(3, points_list, axis_list, 'joint')


if __name__ == '__main__':
    if FLAGS.link_num > 0:
        main_processor(FLAGS.link_num)
    else:
        print('in put number of links')




