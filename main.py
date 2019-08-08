import math

def calc_angle_mbc(a, b):
    theta = math.atan(a/b)
    return round(theta * 180 / math.pi)

