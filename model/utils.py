import matplotlib.image as mpimg
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.python.ops import array_ops

def load_image(path):
    # 读取图片，rgb
    img = mpimg.imread(path)
    # 将图片修剪成中心的正方形
    short_edge = min(img.shape[:2])
    yy = int((img.shape[0] - short_edge) / 2)
    xx = int((img.shape[1] - short_edge) / 2)
    crop_img = img[yy: yy + short_edge, xx: xx + short_edge]
    return crop_img

def resize_image(image, size):
    with tf.name_scope('resize_image'):
        images = []
        for i in image:
            i = cv2.resize(i, size)
            images.append(i)
        images = np.array(images)
        return images

def resize_image_keep_ratio(image, size):
    old_size = image.shape[0:2]
    # ratio = min(float(target_size)/(old_size))
    ratio = min(float(size[i]) / (old_size[i]) for i in range(len(old_size)))
    new_size = tuple([int(i * ratio) for i in old_size])
    img = cv2.resize(image, (new_size[1], new_size[0]))
    pad_w = size[1] - new_size[1]
    pad_h = size[0] - new_size[0]
    top, bottom = pad_h // 2, pad_h - (pad_h // 2)
    left, right = pad_w // 2, pad_w - (pad_w // 2)
    img_new = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, None, (0, 0, 0))
    return img_new

def print_answer(argmax):
    with open("./data/model/index_word.txt","r",encoding='utf-8') as f:
        synset = [l.split(";")[1][:-1] for l in f.readlines()]
        
    print(synset[argmax])
    return synset[argmax]

def preprocess(img):
    img = img / 255
    img = np.expand_dims(img, axis=0)
    img = resize_image(img, (224, 224))
    return img