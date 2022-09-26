import os

data_path = "../datasets/sudoku_img"

with open('train.txt','w') as f:
    label_files = os.listdir(data_path)
    for label_file in label_files:
        label_file_path = os.path.join(data_path, label_file)
        img_files = os.listdir(label_file_path)
        for img_file in img_files:
            img_file_path = os.path.join(label_file_path, img_file)
            f.write(img_file_path + ";" + str(label_file) + "\n")








