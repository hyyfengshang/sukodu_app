import numpy as np

from tools.sudoku_decrypt import Sudoku
from model.model.VGG16 import VGG16
from tools.img_cut import img_cut,display_blocks
from tools.img_detect import img_detect
import cv2
from model.utils import preprocess,resize_image
import time



def predict(img_path):
    img = cv2.imread(img_path)
    t1 = time.time()
    detect_model = VGG16(2)
    detect_model.load_weights('../logs/20220928_img.h5')
    detect_img = img_detect(img)
    detect_result = np.argmax(detect_model.predict(preprocess(detect_img)))
    print("detect_result:", detect_result)
    t2 = time.time()
    print(f"detect time:{t2-t1}")
    if detect_result == 0:
        print('数独图片不符合要求')
        return
    crop_imgs = np.array(img_cut(detect_img))/255
    crop_imgs = resize_image(crop_imgs, (224, 224))
    display_blocks(crop_imgs)
    t3 = time.time()
    model = VGG16(10)
    model.load_weights('../logs/20220925_nums.h5')
    results = model.predict(crop_imgs)
    outs = []
    for result in results:
        out = np.argmax(result)
        # print(out)
        outs.append(out)

    sudoku_example = []

    for i in range(9):
        sudoku_rows = []
        for j in range(9):
            sudoku_rows.append(outs[i*9+j])
        sudoku_example.append(sudoku_rows)
    t4 = time.time()
    print(f'result time:{t4-t3}')

    # print(sudoku_example)
    print("\n获得的数独例子")
    for i in sudoku_example:
        print(i)

    sudo = Sudoku(sudoku_example)
    t5 = time.time()
    result, out = sudo.get_result()
    print("\n得到的数独结果")
    for i in result:
        print(i)
    t6 = time.time()
    print(f"\n耗时:{t6 - t5}秒")
    return result


if __name__ == '__main__':
    img_path = '../imgs/5.jpg'
    predict(img_path)




