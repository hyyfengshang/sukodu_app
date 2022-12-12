MODEL_TYPE = 2
# weight model
if MODEL_TYPE == 0:
    IMG_MODEL_PATH = "../logs/20220926_img.h5"
    NUMS_MODEL_PATH = "../logs/20220925_nums.h5"

# tf model
elif MODEL_TYPE == 1:
    IMG_MODEL_PATH = "../logs/best_img.h5"
    NUMS_MODEL_PATH = "../logs/best_nums.h5"

# onnx model
else:
    IMG_MODEL_PATH = "../logs/best_img.onnx"
    NUMS_MODEL_PATH = "../logs/best_nums.onnx"

DEVICE = "-1"
