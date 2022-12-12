import os
import time

import tensorflow as tf
import numpy as np
import utils
import cv2
from tensorflow.keras import backend as K
from model.VGG16 import VGG16

K.set_image_data_format('channels_last')
model_path = "../logs/best_nums.h5"
img_path = '../datasets/sudoku_nums'

if __name__ == "__main__":
    # os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    # tf.device('/ cpu :0')
    model = tf.keras.models.load_model(model_path)
    label_files = os.listdir(img_path)
    for label_file in label_files:
        label_file_path = os.path.join(img_path,label_file)
        img_files = os.listdir(label_file_path)
        for img_file in img_files:
            img_file_path = os.path.join(label_file_path, img_file)
            img = cv2.imread(img_file_path)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = img/255
            img = np.expand_dims(img,axis = 0)
            img = utils.resize_image(img,(224,224))
            #utils.print_answer(np.argmax(model.predict(img)))
            t1 = time.time()
            out = model.predict(img)
            t2 = time.time()
            print("tf_model_cost: %.4f" %(t2-t1))
            result = np.argmax(out)
            print(result)
            if result != int(label_file):
                print(img_file)
                img = cv2.imread(os.path.join(label_file_path,img_file))
                cv2.imshow(label_file,img)
                cv2.waitKey(0)