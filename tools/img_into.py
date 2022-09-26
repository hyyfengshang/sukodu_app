import io
import base64
from PIL import Image
import cv2
import numpy as np


def image2byte(image):
    '''
    图片转byte
    image: 必须是PIL格式
    image_bytes: 二进制
    '''
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def byte2image(byte_data):
    '''
    byte转为图片
    byte_data: 二进制
    '''
    image = Image.open(io.BytesIO(byte_data))
    return image


def numpy2byte(image):
    '''
    数组转二进制
    image : numpy矩阵/cv格式图片
    byte_data：二进制数据
    '''
    #对数组的图片格式进行编码
    success,encoded_image = cv2.imencode(".jpg",image)
    #将数组转为bytes
    byte_data = encoded_image.tobytes()
    return byte_data
def byte2numpy(byte_data):
    '''
    byte转numpy矩阵/cv格式
    byte_data：二进制数据
    image : numpy矩阵/cv格式图片
    '''
    image = np.asarray(bytearray(byte_data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


if __name__ == '__main__':
    img_path = '../imgs/4.jpg'
    # result = predict(img_path)
    # print(result)
    # img = show_result(result)
    # print(img)
    img = cv2.imread(img_path)
    bytes_img = numpy2byte(img)