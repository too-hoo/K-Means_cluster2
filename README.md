# 使用K-Means对图像进行分割

## 将微信开屏封面进行分割总结

1、使用K-Means对图像进行分割，不难发现其有个缺陷：聚类个数K值需要实现指定。不知道该聚成几类，那么最好会给K值多设置几个点，然后选择聚类结果最好的那个值

2、在整个图像的分割过程中，会发现使用K-means计算的过程在sklearn中就是几行代码，大部分的工作还是在预处理和后处理的基础上。预处理是将图像进行加载，数据规范化。后处理是对决的结果进行反变换。

3、如果涉及后处理，我们也可以自己来设定数据规范化的函数，这样的反变换的函数比较容易编写。

4、另外使用Python对图像进行读写，具体代码如下，上面的代码中也有对应的实现代码：
```
import PIL.Image as image
# 得到图像的像素值
img = image.open(f)
# 得到图像的尺寸
width, height = img.size
```
这里会使用到PIL这个工具包，它的英文全称叫做Python Imaging Library，就是Python的图像处理标准库。同时也使用到了skimage工具包（scikit-image），它也是图像的处理工具包。它和Matlib处理图像相媲美，集成很多的图像处理函数，其中对不同的分类标识显示不同的颜色。在Python中图像的处理工具包，使用的就是skimage工具包。

5、工具的使用和注意点
- K-Means的聚类工具，数据规范化工具，图像处理工具，应用工具进行对图像进行分割
- 不同的尺寸图像，K-Means的运行时间不同。如果尺寸较大，就可以先压缩，长度在200像素内运行的比较快，超过1000像素，速度很慢，例如本例代码

6、KMeans实战
- 聚类工具
    - 创建：kmeans=KMeans(n_cluster=16)
    - 训练：kmeans.fit(data)
    - 预测：kmeans.predict(data)
    - 训练&预测：kmeans.fit_predict(data)
- 数据规范化工具
    - Min-Max规范化：preprocessing.MinMaxScaler()
    - 数据规范化：fit_transform(data)
    - 数据反变换：在Min-Max规范化的时候，自己定义Min-Max的Max值，方便求解反变换的函数。
- 图像处理工具
    - 工具包：PIL.Image,skimage
    - 获取图像文件的内容（像素值）:Image.open(f)
    - 创建新的像素：image=Image.new("RGB", (width, height))
    - 将矩阵转化成为图像：Image.fromarray(label_color)
    - 保存图像：image.save(filename)
    - 将分类标识矩阵转化成为不同颜色的矩阵：(color.label2rgb(label)*255).astype(np.uint8)
