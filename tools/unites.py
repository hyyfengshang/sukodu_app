import time

import cv2
import matplotlib.pyplot as plt


def show(name, img, time_lock=0, width=None, height=None):
    # 显示图片
    cv2.namedWindow(str(name), cv2.WINDOW_NORMAL)
    if not width:
        width = img.shape[0]
    if not height:
        height = img.shape[1]
    cv2.resizeWindow(str(name), width, height)  # 改变窗口大小
    cv2.imshow(str(name), img)
    out = cv2.waitKey(time_lock)
    cv2.destroyAllWindows()
    return out


def plot(img):
    plt.figure()
    plt.imshow(img)
    plt.show(block=False)
    time.sleep(10)
    plt.close('all')


def example_transform(example):
    for index_row,i in enumerate(example):
        for index_line,j in enumerate(i):
            if j == '':
                example[index_row][index_line] = 0
    return example


if __name__ == '__main__':
    img_path = '../imgs/1.jpg'
    img = cv2.imread(img_path)
    plot(img)
    # plt.close(fig=0)
