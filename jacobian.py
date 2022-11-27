import math
import numpy as np


def jacobian_2(length, angle, angular_v):
    j1 = [-length[0] * math.sin(angle[0])
          - length[1] * math.sin(angle[0] + angle[1])
          - length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[0] * math.cos(angle[0])
          + length[1] * math.cos(angle[0] + angle[1])
          + length[2] * math.cos(angle[0] + angle[1] + angle[2])]
    j2 = [-length[1] * math.sin(angle[0] + angle[1])
          - length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[1] * math.cos(angle[0] + angle[1]) +
          length[2] * math.cos(angle[0] + angle[1] + angle[2])]
    j3 = [-length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[2] * math.cos(angle[0] + angle[1] + angle[2])]
    j1 = np.asarray(j1)
    j2 = np.asarray(j2)
    j3 = np.asarray(j3)
    j1 = j1.T
    j2 = j2.T
    j3 = j3.T

    ans = np.dot(j1, angular_v[0])+np.dot(j2, angular_v[1])+np.dot(j3, angular_v[2])
    return ans


def jacobian_matrix(length, angle, angular_v):
    q_di = [angular_v[0], angular_v[1], angular_v[2]]

    j1 = [-length[0] * math.sin(angle[0])
          - length[1] * math.sin(angle[0] + angle[1])
          - length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[0] * math.cos(angle[0])
          + length[1] * math.cos(angle[0] + angle[1])
          + length[2] * math.cos(angle[0] + angle[1] + angle[2])
        , 1]
    j2 = [-length[1] * math.sin(angle[0] + angle[1])
          - length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[1] * math.cos(angle[0] + angle[1]) +
          length[2] * math.cos(angle[0] + angle[1] + angle[2])
        , 1]
    j3 = [-length[2] * math.sin(angle[0] + angle[1] + angle[2])
        , length[2] * math.cos(angle[0] + angle[1] + angle[2])
        , 1]

    j = [j1, j2, j3]
    j = np.asarray(j)
    q_di = np.asarray(q_di)
    j = j.T
    q_di = q_di.T

    # print(j)
    # print(j.shape)
    # print(q_di)
    # print(q_di.shape)

    ans = np.dot(j, q_di)
    # print(ans)


def velocity(length, angle, angular_v):
    x1 = -length[0] * math.sin(angle[0]) * angular_v[0]
    x2 = -length[1] * math.sin(angle[0] + angle[1]) * (angular_v[0] + angular_v[1])
    x3 = -length[2] * math.sin(angle[0] + angle[1] + angle[2]) * (angular_v[0] + angular_v[1] + angular_v[2])

    y1 = length[0] * math.cos(angle[0]) * angular_v[0]
    y2 = length[1] * math.cos(angle[0] + angle[1]) * (angular_v[0] + angular_v[1])
    y3 = length[2] * math.cos(angle[0] + angle[1] + angle[2]) * (angular_v[0] + angular_v[1] + angular_v[2])

    v = [x1 + x2 + x3, y1 + y2 + y3]
    # print(v)
    return v


if __name__ == '__main__':
    # use to test function
    pi = math.pi
    length = np.zeros(3)
    angle = np.zeros(3)
    angular_v = np.zeros(3)

    length[0] = 2
    length[1] = 2
    length[2] = 2

    angle[0] = pi / 6
    angle[1] = pi / 6
    angle[2] = pi / 6

    angular_v[0] = pi / 6
    angular_v[1] = pi / 6
    angular_v[2] = pi / 6

    # jacobian_matrix(length, angle, angular_v)
    # jacobian_2(length, angle, angular_v)
    # ans = velocity(length, angle, angular_v)
    a = [[1,2,3],
         [1,2,4]]
    b = [[1,1,1,0],
         [2,1,1,1],
         [1,1,1,4]]
    print(np.dot(a,b))

