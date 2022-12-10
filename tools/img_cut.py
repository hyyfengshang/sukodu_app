"""将数组图片分成九宫格"""
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import copy as cp
import random
import cv2
import collections
from tools.unites import show


def img_cut(img, m=9, n=9):  # 分割成m行n列
    m += 1
    n += 1
    h, w = img.shape[0], img.shape[1]
    grid_h = int(h * 1.0 / (m - 1) + 0.5)  # 每个网格的高
    grid_w = int(w * 1.0 / (n - 1) + 0.5)  # 每个网格的宽

    # 满足整除关系时的高、宽
    h = grid_h * (m - 1)
    w = grid_w * (n - 1)

    # 图像缩放
    img_re = cv2.resize(img, (w, h),
                        cv2.INTER_LINEAR)  # 也可以用img_re=skimage.transform.resize(imgs, (h,w)).astype(np.uint8)
    # plt.imshow(img_re)
    gx, gy = np.meshgrid(np.linspace(0, w, n), np.linspace(0, h, m))
    gx = gx.astype(np.int)
    gy = gy.astype(np.int)

    divide_image = np.zeros([m - 1, n - 1, grid_h, grid_w, 3],
                            np.uint8)  # 这是一个五维的张量，前面两维表示分块后图像的位置（第m行，第n列），后面三维表示每个分块后的图像信息

    for i in range(m - 1):
        for j in range(n - 1):
            divide_image[i, j, ...] = img_re[
                                      gy[i][j]:gy[i + 1][j + 1], gx[i][j]:gx[i + 1][j + 1], :]
    img_list = []
    m, n = divide_image.shape[0], divide_image.shape[1]
    for i in range(m):
        for j in range(n):
            img = divide_image[i, j, :]
            img_list.append(img)

    return img_list


# 显示图片
def display_blocks(divide_image, m=9, n=9):
    plt.figure(1)
    # print(len(divide_image))
    for i in range(m):
        for j in range(n):
            plt.subplot(m, n, i * n + j + 1)
            plt.imshow(divide_image[i * n + j])
            plt.axis('off')
            # plt.show()
    plt.show()


if __name__ == '__main__':
    img = cv2.imread(r"../imgs/1.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # h, w = imgs.shape[0], imgs.shape[1]
    # fig1 = plt.figure('原始图像')
    # plt.imshow(imgs)
    # plt.axis('off')
    # plt.title('Original image')

    m = 9
    n = 9
    divide_image2 = img_cut(img, m, n)  # 该函数中m+1和n+1表示网格点个数，m和n分别表示分块的块数
    display_blocks(divide_image2)
    # fig3 = plt.figure('分块后的子图像:图像缩放法')
    # for i in divide_image2:
    #     show('i',i)
