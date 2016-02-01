#-*- coding: utf8 -*-
"""
用蒙特卡罗模拟计算pi
"""

import math
import random


def calc_pi(times):
    """
    采用蒙特卡罗算法计算pi
    """
    random.seed()

    in_circle = 0
    for _ in range(times):
        x,y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            in_circle += 1

    return 4*in_circle/times

    
def main():
    for i in range(2, 11):
        times = 10**i
        pi = calc_pi(times)
        sq = abs(pi - math.pi)/math.pi*100
        print("蒙特卡罗模拟次数：{}, 结果：{}, 误差：{}%".format(times, pi, sq))


if __name__ == '__main__':
    main()
