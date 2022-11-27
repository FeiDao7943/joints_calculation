import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
from rotate import z_rot


def draw_fig(num, coor_dic, axi_dic, final_velocity=None, draw_type='None'):
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
            # ax.plot(2+math.pow(2, 0.5), 2+math.pow(2, 0.5), 0, 'o', color=[0, 0, 1])

        if draw_type == 'velocity':
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')


            v_axi = np.zeros((6, 3))
            v_axi[0, :] = coor_dic[-1]
            v_axi[1, :] = [final_velocity[0]/5, final_velocity[1]/5, 0] + coor_dic[-1]
            # v_axi_mid = [0.8*final_velocity[0]/5, 0.8*final_velocity[1]/5, 0] + coor_dic[-1]
            leng = math.pow((math.pow(final_velocity[0], 2) + math.pow(final_velocity[1], 2)), 0.5)
            v_ang = math.atan(abs(final_velocity[1]/final_velocity[0]))
            v_ang_1 = math.pi/2 - v_ang - math.pi/9
            v_ang_2 = math.pi/9 - v_ang
            v_axi[2, :] = v_axi[1, :] + [math.sin(v_ang_1)*leng*0.04, -math.cos(v_ang_1)*leng*0.04, 0]
            v_axi[3, :] = [final_velocity[0] / 5, final_velocity[1] / 5, 0] + coor_dic[-1]
            v_axi[4, :] = v_axi[1, :] + [math.cos(v_ang_2)*leng*0.04, math.sin(v_ang_2)*leng*0.04, 0]
            v_axi[5, :] = [final_velocity[0] / 5, final_velocity[1] / 5, 0] + coor_dic[-1]

            ax.plot(coor_dic[:, 0], coor_dic[:, 1], coor_dic[:, 2], 'o-', color=[0, 0, 1])
            ax.plot(coor_dic[0, 0], coor_dic[0, 1], coor_dic[0, 2], 'o', color=[1, 0, 0])
            ax.plot(v_axi[:, 0], v_axi[:, 1], v_axi[:, 2], '-', color=[55/255, 143/255, 43/255])
            # ax.plot(2+math.pow(2, 0.5), 2+math.pow(2, 0.5), 0, 'o', color=[0, 0, 1])
            for i in range(num+1):
                ax.plot(axi_dic[i, :, 0], axi_dic[i, :, 1], axi_dic[i, :, 2], '-', color=[0.8, 0.8, 0.2])
        plt.show()


def print_part(origin, points_list):
    # print part
    print('origin  : ', end='')
    print('[%.3f, %.3f, %.3f]' % (origin[0], origin[1], origin[2]))
    for i in range(points_list.shape[0]-2):
        print('joint', str(i), ': ', end='')
        # print('[%.3f, %.3f, %.3f]' % (points_list[i + 2][0], points_list[i + 2][1], points_list[i + 2][2]), end='     ')
        print('[%.3f, %.3f, %.3f]' % (points_list[i + 2][0], points_list[i + 2][1], points_list[i + 2][2]))

        alpha_angle = math.atan(points_list[i + 2][1] / points_list[i + 2][0]) / np.pi
        # print('alpha angle: %.3f pi' % alpha_angle)

