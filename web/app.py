import os
from datetime import datetime
import random
from web.image_processor.image_process import img_process

from flask import Flask, render_template, request

app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False

# 获取当前位置的绝对路径，用来存储文件
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET','POST'])
def upload():
    msg = "Error"
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        if 'image' in request.files:
            f = request.files.get('image')
            random_num = random.randint(0, 100)
            filename = datetime.now().strftime("%Y%m%d%H%M%S") + "." + \
                       f.filename.rsplit('.', 1)[1]
            file_path = basedir + "\\static\\file\\" + filename
            # file_path 上传图片存储的位置
            f.save(file_path)
            msg = img_process(file_path)
            return msg
        else:
            return msg
    else:
        return msg

if __name__ == '__main__':
    app.run(debug=True)