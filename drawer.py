# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np


def draw_fig(num, coor_dic, axi_dic, draw_type='None'):
    if not draw_type == 'None':
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_xlim3d(0, 6)
        ax.set_ylim3d(0, 6)
        ax.set_zlim3d(0, 6)
        if draw_type == 'joint':
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.plot(coor_dic[:, 0], coor_dic[:, 1], coor_dic[:, 2], 'o-', color=[0, 0, 1])
            ax.plot(coor_dic[0, 0], coor_dic[0, 1], coor_dic[0, 2], 'o', color=[1, 0, 0])
            for i in range(num+1):
                ax.plot(axi_dic[i, :, 0], axi_dic[i, :, 1], axi_dic[i, :, 2], '-', color=[0.8, 0.8, 0.2])
        plt.show()


def print_part(origin, points_list):
    # print part
    print('origin  : ', end='')
    print('[%.3f, %.3f, %.3f]' % (origin[0], origin[1], origin[2]))
    for i in range(points_list.shape[0]-2):
        print('joint', str(i), ': ', end='')
        print('[%.3f, %.3f, %.3f]' % (points_list[i + 2][0], points_list[i + 2][1], points_list[i + 2][2]), end='     ')
        alpha_angle = math.atan(points_list[i + 2][1] / points_list[i + 2][0]) / np.pi
        print('alpha angle: %.3f pi' % alpha_angle)

