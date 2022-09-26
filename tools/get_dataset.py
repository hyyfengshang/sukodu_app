import os
from tools.img_cut import img_cut, display_blocks
from tools.img_detect import img_detect
import cv2
import shutil
from tools.unites import show, plot
from tools.config import Key

img_path = r'../imgs'
sudoku_path = r'../datasets/sudoku_img'
num_path = r'..\datasets\sudoku_nums'
DE_WEIGHT = True
CROP = False
img_files = os.listdir(img_path)
for i in range(10):
    num_img_path = os.path.join(num_path,str(i))
    if not os.path.exists(num_img_path):
        os.makedirs(num_img_path)
for i in range(2):
    sudoku_img_path = os.path.join(sudoku_path,str(i))
    if not os.path.exists(sudoku_img_path):
        os.makedirs(sudoku_img_path)
# datafiles = os.listdir(datasets_path)
exit_files0 = os.listdir(os.path.join(sudoku_path,'0'))
exit_files1 = os.listdir(os.path.join(sudoku_path,'1'))
# sudoku_num = 1
fig_num = 0
for img_file in img_files:
    print(img_file)
    if img_file in exit_files0 or img_file in exit_files1:
        print(f'{img_file} is exits')
        continue
    img_file_path = os.path.join(img_path, img_file)
    img = cv2.imread(img_file_path)
    if img is None:
        print(f'{img_file}不存在')
        continue
    detect_img = img_detect(img)
    # show('img',detect_img,5000)
    if detect_img is None:
        print(f"{img_file} not detect")
        continue
    crop_imgs = img_cut(detect_img, 9, 9)
    display_blocks(crop_imgs)
    fig_num += 1
    sudoku_mode = str(input("输入图片标签:"))
    while sudoku_mode != '0' and sudoku_mode != '1':
        # show('img', detect_img, 5000)
        # display_blocks(crop_imgs)
        sudoku_mode = str(input("输入的标签不存在，请重新输入:"))
    # sudoku_img_name = str(sudoku_num) + '.jpg'
    # if DE_WEIGHT:
    #     exit_files = os.listdir(os.path.join(sudoku_path,sudoku_mode))
    #     while sudoku_img_name in exit_files:
    #         sudoku_num += 1
    #         sudoku_img_name = str(sudoku_num) + '.jpg'
    save_sudoku_path = os.path.join(sudoku_path, sudoku_mode)
    # exit_files = os.listdir(save_sudoku_path)
    # if img_file in exit_files:
    #     print(f'{img_file}已存在!')
    #     continue
    save_sudoku_file_path = os.path.join(save_sudoku_path,img_file)
    # shutil.copy(img_file_path, save_sudoku_path)
    cv2.imwrite(save_sudoku_file_path, detect_img)
    if int(sudoku_mode) == 1 and CROP:
        print(f'剪切{img_file}')
        for crop_img in crop_imgs:
            out = str(show('img', crop_img, 0, 500, 500))
            while out not in Key.keys():
                out = str(show('img', crop_img, 0, 500, 500))
            num_mode = str(Key[out])
            nums_num = 1
            num_name = str(nums_num)+'.jpg'
            if DE_WEIGHT:
                exit_num_files = os.listdir(os.path.join(num_path,num_mode))
                while num_name in exit_num_files:
                    nums_num += 1
                    num_name = str(nums_num) + '.jpg'
            save_num_path = os.path.join(num_path, num_mode,num_name )
            cv2.imwrite(save_num_path, crop_img)
            # nums_num += 1




