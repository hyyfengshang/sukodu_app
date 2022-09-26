"""对数独图片进行处理，裁剪包含数独的矩形框"""
import os
import cv2
import copy
import numpy as np
from tools.unites import show

# img_path = '../imgs/1.jpg'

# fun1
# imgs = cv2.imread(r'../imgs/1.jpg', 0)
# h, w = imgs.shape[:2]
# imgray = 255 - imgs
# ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# rects = [cv2.boundingRect(cnt) for cnt in contours]
# top_x = min([x for (x, y, w, h) in rects])
# top_y = min([y for (x, y, w, h) in rects])
# bottom_x = max([x + w for (x, y, w, h) in rects])
# bottom_y = max([y + h for (x, y, w, h) in rects])
# out = cv2.rectangle(imgs, (top_x, top_y), (bottom_x, bottom_y), (0, 255, 0), 2)
# cv2.imwrite('out.jpg', imgs)


# fun2
def img_detect(image):
    # image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width = image.shape[0]
    height = image.shape[1]
    # show('blank_img', blank_img)
    # show('gray',gray)

    # gradX1 = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    # show('x1', gradX1)
    # gradX2 = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1)
    # show('x2', gradX2)
    # gradX3 = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
    # show('x3', gradX3)
    # gradX4 = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=5)
    # show('x4', gradX4)
    # gradX5 = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=7)
    # show('x5', gradX5)
    # gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
    # subtract the y-gradient from the x-gradient
    # show('y',gradY)
    # gradient = cv2.subtract(gradX, gradY)

    # sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    # sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    # sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
    # sobely = cv2.convertScaleAbs(sobely)
    # gradient = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    # show('grand',gradient)
    gradient = cv2.convertScaleAbs(gray)
    # show('grand',gradient)
    cv2.bitwise_not(gradient, gradient)   # 取反
    # show('grand',gradient)
    # blurred = cv2.blur(gradient, (9, 9))
    # show('blurred',blurred)
    (_, thresh1) = cv2.threshold(gradient, 90, 255, cv2.THRESH_BINARY)
    (_, thresh2) = cv2.threshold(gradient, 150, 255, cv2.THRESH_BINARY)
    # show('thresh1', thresh1)
    # show('thresh2', thresh2)
    # th1 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1, dst=None)
    # show('th1', th1)
    # th2 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 1, dst=None)
    # show('th2', th2)
    # th3 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 10, dst=None)
    # show('th3', th3)
    # th4 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 10, dst=None)
    # show('th4', th4)
    # th5 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 50, dst=None)
    # show('th5',th5)
    # th6 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 100, dst=None)
    # show('th6', th6)
    # th7 = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 150, dst=None)
    # show('th7', th7)
    (cnts1, _) = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (cnts2, _) = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('轮廓框的个数1：{}'.format(len(cnts1)))
    # print('轮廓框的个数2：{}'.format(len(cnts2)))
    # 最低线段的长度，小于这个值的线段被抛弃
    # minLineLength = height / 2
    # # 线段中点与点之间连接起来的最大距离，在此范围内才被认为是单行
    # maxLineGap = 100
    # lines = cv2.HoughLinesP(gradient, 1, np.pi/180, 100, minLineLength, maxLineGap)
    # blank_img = np.zeros((width, height, 3), np.uint8)
    #
    # for i in range(len(lines)):
    #     for x1, y1, x2, y2 in lines[i]:
    #         cv2.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # show('draw', blank_img)

    # hline = cv2.getStructuringElement(cv2.MORPH_RECT, (int(image.shape[1] / 16), 1), (-1, -1))
    #
    # vline = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(image.shape[0] / 16)), (-1, -1))
    #
    # blank_img = np.zeros((width, height, 3), np.uint8)
    # dst = cv2.morphologyEx(blank_img, cv2.MORPH_OPEN, vline)
    # dst = cv2.bitwise_not(dst)
    # show('dst',dst)

    # x_min = width
    # y_min = height
    # x_max = 0
    # y_max = 0
    # for cnt in cnts:
    #     for points in cnt:
    #         for point in points:
    #             print(point)
    #             x = point[0]
    #             y = point[1]
    #             if x < x_min:
    #                 x_min = x
    #             if x > x_max:
    #                 x_max = x
    #             if y < y_min:
    #                 y_min = y
    #             if y > y_max:
    #                 y_max = y

    # for cnt in cnts:
    #     blank_img = np.zeros((width, height, 3), np.uint8)
    #     # show('blank', blank_img)
    #     cv2.drawContours(blank_img, cnt, -1, (0, 0, 255), 3)
    #     show('draw',blank_img)
    # blank_img = np.zeros((width, height, 3), np.uint8)
    # cv2.drawContours(blank_img, cnts, -1, (0, 0, 255), 3)
    # show('draw', blank_img)
    # all_box_img = copy.deepcopy(image)
    #
    c1 = sorted(cnts1, key=cv2.contourArea, reverse=True)
    c2 = sorted(cnts2, key=cv2.contourArea, reverse=True)
    if len(c1) == 0 or len(c2) == 0:
        return image
    rect1 = cv2.minAreaRect(c1[0])
    rect2 = cv2.minAreaRect(c2[0])
    box1 = np.int0(cv2.boxPoints(rect1))
    box2 = np.int0(cv2.boxPoints(rect2))
    # draw a bounding box arounded the detected barcode and display the image
    top1_box_img = copy.deepcopy(image)
    top2_box_img = copy.deepcopy(image)
    cv2.drawContours(top1_box_img, [box1], -1, (0, 255, 0), 1)
    cv2.drawContours(top2_box_img, [box2], -1, (0, 255, 0), 1)
    # show('counter1', top1_box_img, num=2000)
    # show('counter2', top2_box_img, num=2000)
    # show('counter2', top1_box_img)
    x_box1 = [i[0] for i in box1]
    y_box1 = [i[1] for i in box1]
    x1 = x_box1
    y1 = y_box1
    x1_min = 0 if min(x1) < 0 else min(x1)
    x1_max = 0 if max(x1) < 0 else max(x1)
    y1_min = 0 if min(y1) < 0 else min(y1)
    y1_max = 0 if max(y1) < 0 else max(y1)

    x_box2 = [i[0] for i in box2]
    y_box2 = [i[1] for i in box2]
    x2 = x_box2
    y2 = y_box2
    x2_min = 0 if min(x2) < 0 else min(x2)
    x2_max = 0 if max(x2) < 0 else max(x2)
    y2_min = 0 if min(y2) < 0 else min(y2)
    y2_max = 0 if max(y2) < 0 else max(y2)

    area1 = (x1_max - x1_min) * (y1_max - y1_min)
    area2 = (x2_max - x2_min) * (y2_max - y2_min)
    # if area1 > area2 and area1 * 0.9 > area2:
    if area1 > area2 > area1 * 0.9:
        cropImg = image[y2_min:y2_max, x2_min:x2_max]
    elif area1 > area2:
        cropImg = image[y1_min:y1_max, x1_min:x1_max]
    else:
        cropImg = image[y2_min:y2_max, x2_min:x2_max]

    return cropImg
    # # 查看参数：
    # # print(box0,box1)
    # print('x1:{} x2:{} y1:{} y2:{}'.format(x1, x2, y1, y2))  # 横坐标是x，纵坐标是y
    #
    # # cv2.imshow("all_box_img", all_box_img)
    # # cv2.imshow("top2_box_image1", top2_box_img)
    # cv2.imshow("corped_image", cropImg)
    # # cv2.imwrite("corped_image.jpg", image)
    # cv2.waitKey(0)
    # return cropImg


if __name__ == '__main__':
    # import os
    # imgfiles = os.listdir("../imgs")
    # for img_file in imgfiles:
    #     img_path = "../imgs/" + img_file
    #     img = cv2.imread(img_path)
    #     img = img_detect(img)
    #     cv2.imshow('img',img)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    imgs_path = '../imgs'
    img_files = os.listdir(imgs_path)

    for img_file in img_files:
        img_path = os.path.join(imgs_path, img_file)
        img = cv2.imread(img_path)
        if img is None:
            print(f'{img_file} can not open')
            continue
        img_out = img_detect(img)
        show(f'{img_file}:input', img)
        if img_out is None:
            print(f'{img_file} not get count')
            continue
        show(f'{img_file}:output',img_out)
    img_path = '../imgs/124.jpg'
    img = cv2.imread(img_path)
    show('input', img)
    img = img_detect(img)
    show('output', img)
