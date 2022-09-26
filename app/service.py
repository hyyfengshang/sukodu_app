# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run inference on images, videos, directories, streams, etc.

Usage:
    $ python path/to/detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
"""

import cv2
import numpy as np
import tensorflow as tf
from model.model.VGG16 import VGG16
from model.utils import resize_image
from tools import img_cut, img_detect


class ImgDetect:
    def __init__(self, model_path, class_num):
        # Initialize
        self.cuda = tf.test.is_built_with_cuda
        self.device = tf.device('cuda:0' if self.cuda else 'cpu')

        # Load model
        self.model = VGG16(class_num)
        self.model.load_weights(model_path)
        self.imgsz = 640

    def inference(self, img):
        """
        模型推理，获取目标检测的结果，并根据目标检测的结果进行抠图
        :param img: 输入图片
        :return:
        """
        img = self.preprocess(img)
        pre = self.model.predict(img)
        result = np.argmax(pre)
        return result

    def preprocess(self, img):
        img = img / 255
        img = np.expand_dims(img, axis=0)
        img = resize_image(img, (224, 224))
        return img


class NumDetect:
    def __init__(self, model_path, class_num):
        self.cuda = tf.test.is_built_with_cuda
        self.device = tf.device('cuda:0' if self.cuda else 'cpu')

        # Load model
        self.model = VGG16(class_num)
        self.model.load_weights(model_path)
        self.imgsz = 640

    def inference(self, imgs):
        """
        模型推理，获取目标检测的结果，并根据目标检测的结果进行抠图
        :param img: 输入图片
        :return:
        """
        imgs = self.preprocess(imgs)
        results = self.model.predict(imgs)
        out = self.postprocess(results)
        return out

    @staticmethod
    def preprocess(imgs):
        imgs = resize_image(imgs, (224, 224))/255
        return imgs

    def postprocess(self,results):
        result = [np.argmax(i) for i in results]
        outs = []
        for i in range(9):
            rows = []
            for j in range(9):
                out = result[i * 9 + j]
                rows.append(out)
            outs.append(rows)
        return outs


if __name__ == "__main__":
    # model = ImgDetect("../logs/20220926_img.h5",2)
    # import glob
    #
    # files = glob.glob(r"../datasets/sudoku_img/0/*.jpg")
    # for i in range(len(files)):
    #     print(files[i])
    #     img = cv2.imread(files[i])
    #     ret = model.inference(img)
    #     print(ret)

    model = NumDetect(model_path="../logs/20220925_nums.h5",class_num=10)
    import glob

    files = glob.glob(r"../datasets/sudoku_img/1/*.jpg")
    for i in range(len(files)):
        img = cv2.imread(files[i])
        ret = model.inference(img)
        print(ret)
