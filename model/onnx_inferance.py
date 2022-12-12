import time

import onnxruntime as ort
import os
import cv2
import numpy as np
import utils


print(ort.__version__)
print(ort.get_device())
print(ort.get_available_providers())

if __name__ == "__main__":
    model = ort.InferenceSession("../logs/best_nums.onnx", providers=['CPUExecutionProvider'])  # "CUDAExecutionProvider"
    # print(ort.get_providers())
    img_path = '../datasets/sudoku_nums'
    inputs = model.get_inputs()[0].name
    outputs = model.get_outputs()[0].name
    # for i in outputs:
    #     print(i.nam
    label_files = os.listdir(img_path)
    for label_file in label_files:
        label_file_path = os.path.join(img_path, label_file)
        img_files = os.listdir(label_file_path)
        for img_file in img_files:
            img_file_path = os.path.join(label_file_path, img_file)
            img = cv2.imread(img_file_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # img = np.transpose(img,[2,0,1])
            img = img / 255
            img = np.expand_dims(img, axis=0)
            img = utils.resize_image(img, (224, 224))
            img = np.array(img,dtype=np.float32)
            # utils.print_answer(np.argmax(model.predict(img)))
            t1 = time.time()
            out = model.run([outputs], {inputs:img})
            t2 = time.time()
            print("onnx_cost:%.2f"% (t2-t1))
            result = (np.argmax(out))
            print(result)
            if result != int(label_file):
                print(img_file)
                img = cv2.imread(os.path.join(label_file_path, img_file))
                cv2.imshow(label_file, img)
                cv2.waitKey(0)
