from enum import Enum
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
import base64
import numpy as np
from PIL import Image
import cv2
from tools.img_into import numpy2byte
from model.utils import resize_image


class ErrorMsg(Enum):
    ILLEGAL_INPUT = (101, "非法的输入")
    ILLEGAL_INPUT_SIZE = (102, "非法的图片大小")
    NO_CATTLE_DETECT = (103, "图片输入不符合要求")
    INVALID_TOKEN = (104, "非法的token")


Num_Colors = {
    "0": (255, 255, 255),
    "1": (0, 255, 255),
    "2": (255, 235, 205),
    "3": (118, 238, 198),
    "4": (112, 128, 144),
    "5": (0, 255, 0),
    "6": (0, 0, 255),
    "7": (255, 255, 0),
    "8": (255, 0, 0),
    "9": (148, 0, 211),
}


#
# Num_Colors = {
#     "0": 'w',
#     "1": 'c',
#     "2": 'g',
#     "3": 'm',
#     "4": 'y',
#     "5": 'l',
#     "6": 'b',
#     "7": 'h',
#     "8": 'j',
#     "9": 'r',
# }

def show_result(result):
    result.reverse()
    plt.figure(figsize=(9, 9))  # 设置画布大小
    ax = plt.gca()  # 获取画布
    x_major_locator = MultipleLocator(1)  # 定义刻度值
    y_major_locator = MultipleLocator(1)
    ax.xaxis.set_major_locator(x_major_locator)  # 设置刻度值
    ax.yaxis.set_major_locator(y_major_locator)
    cm = plt.cm.get_cmap('rainbow', 10)  # 分为7级
    ax.set(xlim=(0, 9), ylim=(0, 9))  # 设置想x，y刻度值区间
    plt.xticks([])  # 隐藏想坐标值
    plt.yticks([])
    for i, rows in enumerate(result):
        for j, value in enumerate(rows):
            plt.scatter(j + 0.5, i + 0.5, marker=',', s=3100,
                        c=value, vmin=0, vmax=9, cmap=cm)  # 画像素块
            ax.text(j + 0.5, i + 0.5, value, size=20, va="center", ha="center")  # 写文字
    fig = plt.gcf().canvas  # 获取当前图像并添加画布
    ag = fig.switch_backends(FigureCanvasAgg)
    ag.draw()
    A = np.asarray(ag.buffer_rgba())
    pil_img = Image.fromarray(A)
    pil_img = pil_img.convert('RGB')
    img = np.asarray(pil_img)
    return img


def RGB_to_Bytes(img):
    img_bytes = BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    img.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def return_img_stream(img, resize=None):
    if resize:
        img = cv2.resize(img, resize)
    img_bytes = numpy2byte(img)
    img_stream = base64.b64encode(img_bytes).decode()
    return img_stream


def post_process(img):
    img = img / 255
    img = np.expand_dims(img, axis=0)
    img = resize_image(img, (224, 224))
    return img


if __name__ == '__main__':
    from tools.predict import predict

    img_path = '../imgs/4.jpg'
    # result = predict(img_path)
    # print(result)
    # img = show_result(result)
    # print(img)
    img = cv2.imread(img_path)
    bytes_img = RGB_to_Bytes(img)
