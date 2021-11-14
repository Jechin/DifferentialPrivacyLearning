# Notes for Reading

## 基于差分隐私的数据发布方法_刘鑫

### 轨迹数据的隐私保护

1. L-轨迹：截止到当前时刻 k，长度为 L 的移动对象 u 的时空点按照时间递增的有序集合
2. 计数查询：也叫数据发布，例如查询结果为时刻 i 各个地点的移动对象的个数
3. 范围查询 Q(Di，start_loc,end_loc):查询时刻 i 从位置 start_loc 到 end_loc 连续区域内(start_loc，end_loc)移动对象的计数之和。

### 基于差分隐私的直方图发布方法 APG（AP聚类）

使用一半的隐私预算对直方图的桶进行排序，使用一般的隐私预算对其进行AP聚类分组

### 基于差分隐私的实时轨迹发布方法 RTPM

该方法首先使用指数衰减机制为当前时间确定隐私预算的大小，将隐私预算相同的分为一组。对于隐私预算相
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

由于p级数的收敛值难以计算（目前只对正偶数的p有公式计算），因此引入**近似p级数的隐私预算分配**

### 隐私预算的分配--基于近似p级数展开

目前存在对p级数收敛值的估计和误差:
$$
M_p \in \left[\frac{1}{p-1}, 1 + \frac{1}{p-1}\right], p>1
$$
因此可以使用 $A_p = 1 + \frac{1}{p-1}$来近似 $M_p$
$$
\varepsilon_i = \frac{\varepsilon}{A_p}\frac{1}{i^p}
$$
但是，这会导致隐私预算总量𝜀不能充分分配，即无论查询多少次，隐私预算的利用率无法达到最大，存在隐私预算浪费问题。 也就是说，近似𝑝级数法引入了更多的噪声。

### 隐私预算的分配--基于建模p级数展开

因为近似p级数的隐私预算利用不充分、不可控，所以基于前有限次 $n_0$的查询类型，引入了建模p级数的隐私预算分配。

其主要思路是，将隐私预算的分配分为两块分别为前 $n_0$次和 $n_0$次之后，分别分配隐私预算 $t \cdot \varepsilon$ 和 $(1-t)\cdot \varepsilon$，其中 $t<1$，二者相加为总的隐私预算。

前 $n_0$次基于p级数的隐私预算分配因为分配次数的有限性，导致p指数的和可以轻易计算得，因此，在前 $n_0$次的隐私预算 $t \cdot \varepsilon$可以被完全分配。

$n_0$次之后的隐私预算分配因为无法保证其理想性或可用性，使用二分法进行分配。

![image-20211112210748866](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211112210748866.png)

#### 噪声评估因子

![image-20211112212553903](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211112212553903.png)

#### 在建模p级数的隐私预算分配中p的选择

较小的𝑝可能意味着较小的噪声评估因子。我们希望找到一个尽量大的p满足，在 $n_0$次的隐私预算分配中使得因素预算大于一个下界以满足隐私预算的合理性（查询的有效性）。

设置函数：$r_n(p) = \frac{t \varepsilon}{n_0^{p+1}}$，如果对任意 $n \leq n_0$，都有 $r_n(p) \geq r'$，则称该建模p级数方法是 $(\varepsilon, n_0, r', t)$-理想隐私预算分配方法。

在这个理想状态下，有：
$$
p = \log _{n_0} (\frac{t \varepsilon}{r'}) - 1
$$

## 车联网中轨迹数据发布隐私保护关键技术的研究_包先跃

### LBS服务模型Location Based Server

车辆向LBS服务器发送请求，实际上是RSU进行转发，（添加换名，映射）

![image-20211114161007918](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211114161009214.png)

### 连续时刻下轨迹隐私保护算法

![image-20211114161350921](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211114161350921.png)

主要是用三种算法：

1. 轨迹粒度分层
2. 假名置换
3. 噪声

#### 轨迹粒度分层

将轨迹分为粗粒度和细粒度：

- 在1个RSU分为内的轨迹移动：细粒度，通过添加噪声来
- 多个RSU之间的轨迹移动：粗粒度，可以使用RSU的位置来代替车辆的准确位置

#### 假名置换

主要是用高斯机制，在当前RSU中其他发出LBS请求的车辆中随机选取一个作为假名并在RSU中存储映射关系。随机选取的概率和距离当前车辆的距离有关，距离越远，被选择的概率就越高。

![image-20211114170220925](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211114170220925.png)

#### 添加噪声

其主要思想是对移动用户的坐标位置添加Laplace噪声，主要优化在于提出了“隐私圈”，计算敏感度，同时提出了收敛精炼（加上噪声后若超出隐私圈，则利用隐私圈半径取余收敛到隐私圈内）

![image-20211114200808476](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211114200808476.png)

![image-20211114200932788](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211114200932788.png)

### K-匿名化的轨迹分段隐私保护

不做深入研究

