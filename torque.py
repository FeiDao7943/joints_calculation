import math
import numpy as np


def torque_cal(link_length, angle, force_x, force_y):
    torque_list = np.zeros(3)
    torque_list[0] = force_y * (+ link_length[0] * math.cos(angle[0])
                           + link_length[1] * math.cos(angle[0] + angle[1])
                           + link_length[2] * math.cos(angle[0] + angle[1] + angle[2])) + \
                force_x * (-link_length[0] * math.sin(angle[0])
                           - link_length[1] * math.sin(angle[0] + angle[1])
                           - link_length[2] * math.sin(angle[0] + angle[1] + angle[2]))
    torque_list[1] = force_y * (+ link_length[1] * math.cos(angle[0] + angle[1])
                           + link_length[2] * math.cos(angle[0] + angle[1] + angle[2])) + \
                force_x * (-link_length[1] * math.sin(angle[0] + angle[1])
                           - link_length[2] * math.sin(angle[0] + angle[1] + angle[2]))
    torque_list[2] = force_y * (+ link_length[2] * math.cos(angle[0] + angle[1] + angle[2])) + \
                force_x * (-link_length[2] * math.sin(angle[0] + angle[1] + angle[2]))
    return torque_list
