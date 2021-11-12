# Notes for Reading

## 基于差分隐私的数据发布方法_刘鑫

### 轨迹数据的隐私保护

1. L-轨迹：截止到当前时刻 k，长度为 L 的移动对象 u 的时空点按照时间递增的有序集合
2. 计数查询：也叫数据发布，例如查询结果为时刻 i 各个地点的移动对象的个数
3. 范围查询 Q(Di，start_loc,end_loc):查询时刻 i 从位置 start_loc 到 end_loc 连续区域内(start_loc，end_loc)移动对象的计数之和。

### 基于差分隐私的直方图发布方法 APG（AP聚类）

使用一半的隐私预算对直方图的桶进行排序，使用一般的隐私预算对其进行AP聚类分组

### 基于差分隐私的实时轨迹发布方法 RTPM

该方法首先使用指数衰
减机制为当前时间确定隐私预算的大小，将隐私预算相同的分为一组。对于隐私预算相
同的数据使用第三章的 APG 方法对数据进行处理。后面对 RTPM 方法进行实验验证，
实验表明 RTPM 方法在满足差分隐私的同时具有较好的可用性。



## 差分隐私保护中隐私预算的优化与应用_王璇

隐私保护数据发布作为差分隐私一个重要研究方向，其发布机制可以分成四类[Differentially private data publishing and analysis]：数据集重构、数据集分割、查询分离和迭代机制

### 隐私预算的分配--基于Taylor展开

![](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211112203558572.png)

Taylor展开级数法需要选定首次预算分配量,即k值,且0<k<1,k值一旦确定,则隐私预算序列{ε}确定。不同的k值决定了不同的隐私预算序列{ε}。因此,与二分法相比, Taylor展开级数法具有可调节性

### 隐私预算的分配--基于p级数展开

p级数：当 $p>1$时级数收敛 计为 $M_p$
$$
\sum_{n=1}^{\infty} \frac{1}{n^p}
$$
![image-20211112204258198](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211112204258198.png)

当 $p=2$时，$M_p = \frac{\pi^2}{6}$, $\varepsilon_i = \frac{6}{\pi^2}\frac{1}{i^2}$



