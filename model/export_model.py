import tensorflow as tf
from model.VGG16 import VGG16

class_num = 10
weight_path = "../logs/20220925_nums.h5"
model_path = "../logs/best_nums.h5"

model = VGG16(class_num)

# 注意要开启skip_mismatch和by_name
model.load_weights(weight_path, by_name=True, skip_mismatch=True)
model.save(model_path)


model = tf.keras.models.load_model(model_path)