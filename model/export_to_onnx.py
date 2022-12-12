import tf2onnx
import tensorflow as tf

onnx_path = "../logs/best_nums.onnx"
model_path = "../logs/best_nums.h5"
spec = (tf.TensorSpec((None, 224, 224, 3), tf.float32, name="input"),)
model = tf.keras.models.load_model(model_path)
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=13, output_path=onnx_path)




