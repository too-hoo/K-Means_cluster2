# -*- coding:utf-8 -*-
# 使用K-Means对图像进行聚类，显示分割标识的可视化
import numpy as np
# 使用pillow包里面的图像模块
import PIL.Image as image
from sklearn.cluster import KMeans
from sklearn import preprocessing
from skimage import color 

# 加载图像，并对数据进行规范化
def load_data(filePath):
    f = open(filePath,'rb')
    data = []
    # 得到图像的像素值
    img = image.open(f)
    # 得到图像的尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点(x,y)的三个通道值
            c1, c2, c3 = img.getpixel((x,y))
            data.append([c1,c2,c3])
    f.close()
    # 采用Min-Max规范化
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height

# 加载图像，得到规范化的结果 img，以及图像的尺寸
img, width, height = load_data('./weixin.jpg')

# 用K-Means对图像进行2聚类
kmeans = KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
# 将图像聚类结果，转化成为图像的尺寸的矩阵
label = label.reshape([width, height])
# 创建个新的图像 pic_mark,用来保存图像的聚类的结果，并设置不同的灰度值
pic_mark = image.new("L", (width, height))
for x in range(width):
    for y in range(height):
        # 根据类别设置图像的灰度，类别 0灰度值为255， 类别1灰度值为127
        pic_mark.putpixel((x,y), int(256/(label[x][y]+1))-1)
pic_mark.save("weixin_mark.jpg", "JPEG")


# 将聚类标识矩阵转化成为不同颜色的矩阵
label_color = (color.label2rgb(label)*255).astype(np.uint8)
# 需要将第一维和第二维颠倒过来
label_color = label_color.transpose(1,0,2)
images = image.fromarray(label_color)
images.save('weixin_mark_color.jpg')