# Flask-Simple-Application

This project is about a simple application of Flask: including uploading files to the backend through the web and calling an image recognition method that was pre written.

这个项目是关于flask的简单应用：包括文件通过web上传到后端以及调用提前写死的一个图像识别。

# 环境配置（Environmental configuration）

pip install numpy

pip install flask

pip install imutils

pip install scipy

pip install opencv-python
 
# 简介（brief introduction）

起初只是想简单的 web 上传图片直接识别，但是出现了一些问题，后面我发现封装好的函数里面的图片读取需要用到文件的绝对路径，所以不得不将文件通过 web 上传至后端，然后通过传递参数 filename 给该函数然后返回正确率的结果。注意的是在 /web/static/file 下面放了一张示例照片，img_process 仅对这一张样例图片有效果，上传其他的图片可能会报错，因为最初的目的并不是识别所有的图片，该函数已经写死了。

At first, I just wanted to simply upload images to the web for direct recognition, but there were some issues. Later, I found that the image reading in the encapsulated function requires the absolute path of the file, so I had to upload the file to the backend through the web, pass the parameter filename to the function, and then return the correct result. Note that a sample photo has been placed under/web/static/file, img_ Process only works on this sample image. Uploading other images may result in an error, as the original purpose was not to recognize all images, and this function has been written dead.

image_processor/image_process.py  def img_process(filename): 函数是写死的，所以上传其他的图片识别不出来就会报错，这个里面可以改成您用深度学习训练之后的模型。示例图片上传之后会返回一组对照图片。

Image_ Processor/image_ Process.py def img_ Process (filename): The function is written dead, so uploading other images that cannot be recognized will result in an error. This can be changed to the model you have trained with deep learning. After uploading the sample images, a set of control images will be returned.

注意（note）：

位于 static 文件夹下面的资源不要随意更改，否者可能会出现失效的情况，比如 css 文件， 还有 （png,jpg) 文件。

Resources located under the static folder should not be changed arbitrarily, otherwise they may become invalid, such as CSS files and (png, jpg) files.
