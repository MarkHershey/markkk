# source author：Moenova
# source：https://zhuanlan.zhihu.com/p/336706023
import numpy as np


def _getA():
    Krgb = np.array([0.299, 0.587, 0.114])
    R = np.array([0.64, 0.33, Krgb[0]])
    G = np.array([0.3, 0.6, Krgb[1]])
    B = np.array([0.15, 0.06, Krgb[2]])
    W = (R + G + B) / 3
    W[2] = 0
    A = (np.array([R, G, B]) - W).T
    return A


def _hsl2rgb(hsl_s):
    # hsl_s  Nx3
    x_s = hsl_s[:, 1] * np.cos(hsl_s[:, 0])
    y_s = hsl_s[:, 1] * np.sin(hsl_s[:, 0])
    l_s = hsl_s[:, 2]
    right_s = np.concatenate([x_s[:, None], y_s[:, None], l_s[:, None]], axis=1)
    A = _getA()
    left_s = np.repeat(A.reshape(1, 3, 3), len(right_s), axis=0)
    rgb_s = np.linalg.solve(left_s, right_s)
    return rgb_s


def _getRGBs(S, L, num=50, targNum=50):
    hs = np.linspace(0, 2 * np.pi, num)
    ss = np.ones(num) * S
    ls = np.ones(num) * L
    hsl_s = np.concatenate([aray[:, None] for aray in [hs, ss, ls]], axis=1)
    rgb_s = _hsl2rgb(hsl_s)

    buffer_rgb_s = []
    for rgb in rgb_s:
        if np.all(rgb >= 0) and np.all(rgb <= 1):
            buffer_rgb_s.append(rgb)
    buffer_rgb_s = np.array(buffer_rgb_s)
    buffer_num = buffer_rgb_s.shape[0]

    if 0 < buffer_num < targNum:
        fix_num = int(num ** 2 / buffer_num) + 5
        buffer_rgb_s = _getRGBs(S, L, num=fix_num, targNum=targNum)

    return buffer_rgb_s


def _getRGBAs(S, L, num):
    # S: 人眼视觉饱和度
    # L: 人眼视觉亮度
    # num: 颜色个数
    rgb_s = _getRGBs(S, L, num=num, targNum=num)
    rgba_s = np.concatenate((rgb_s, np.ones((len(rgb_s), 1))), axis=1)
    print(f"{num}/{len(rgba_s)}")
    return rgba_s


def _clamp(x):
    return max(0, min(x, 255))


def getHexColorList(S, L, num=50):
    hexColorList = []
    rgb_s = _getRGBs(S, L, num=num, targNum=num)
    for i in rgb_s:
        r = int(255 * i[0])
        g = int(255 * i[1])
        b = int(255 * i[2])
        hexColorList.append(
            "#{0:02x}{1:02x}{2:02x}".format(_clamp(r), _clamp(g), _clamp(b)).upper()
        )

    return hexColorList


if __name__ == "__main__":
    print(getHexColorList(0.05, 0.8, 10))
