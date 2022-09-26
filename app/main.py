# -*- coding: utf-8 -*-

import sys
from flask import Flask, jsonify, request, make_response
from service import ImgDetect, NumDetect
from utils import show_result, return_img_stream
from flask import render_template
import numpy as np
from PIL import Image
from tools.sudoku_decrypt import Sudoku
from tools import img_detect, img_cut
import time

sys.path.append(".")
sys.path.append("..")
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])
detect_model = ImgDetect("../logs/20220926_img.h5", 2)
num_model = NumDetect("../logs/20220925_nums.h5", 10)
SIZE = (640, 640)


@app.route('/')
def app_index():
    return render_template('index.html')


@app.route('/app', methods=['GET', 'POST'])
def sudoku():
    return render_template('sukodu.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传文件
@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    t1 = time.time()
    data_file = request.files['photo']
    if data_file and allowed_file(data_file.filename):
        pil_img = Image.open(data_file)
        pil_img = pil_img.convert('RGB')
        img = np.asarray(pil_img)
        detect_img = img_detect.img_detect(img)
        img_in = return_img_stream(detect_img, SIZE)
        detect = detect_model.inference(detect_img)
        if detect == 1:
            cut_imgs = img_cut.img_cut(detect_img)
            pred = num_model.inference(cut_imgs)
            sudo = Sudoku(pred)
            result, msg = sudo.get_result()
            if msg is False:
                return render_template('error_request.html', img_in=img_in, error="图片不符合解密要求")
            img_result = show_result(result)
            img_out = img_detect.img_detect(img_result)
            img_out = return_img_stream(img_out, SIZE)
            t2 = time.time()
            return render_template('show_result.html', img_in=img_in, img_out=img_out, time=str(t2 - t1))
        else:
            return render_template('error_request.html', img_in=img_in, error="图片不符合解密要求")
    else:
        return render_template('error_format.html', error="图片格式错误")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, threaded=True)
