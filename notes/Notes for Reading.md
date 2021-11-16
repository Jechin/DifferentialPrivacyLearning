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

当 $p=2$时，$M_p = \dfrac{\pi^2}{6}$, $\varepsilon_i = \dfrac{6}{\pi^2}\dfrac{1}{i^2}$

由于p级数的收敛值难以计算（目前只对正偶数的p有公式计算），因此引入**近似p级数的隐私预算分配**

### 隐私预算的分配--基于近似p级数展开

目前存在对p级数收敛值的估计和误差:
$$
M_p \in \left[\frac{1}{p-1}, 1 + \frac{1}{p-1}\right], p>1
$$
因此可以使用 $A_p = 1 + \dfrac{1}{p-1}$来近似 $M_p$
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

设置函数：$r_n(p) = \dfrac{t \varepsilon}{n_0^{p+1}}$，如果对任意 $n \leq n_0$，都有 $r_n(p) \geq r'$，则称该建模p级数方法是 $(\varepsilon, n_0, r', t)$-理想隐私预算分配方法。

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

## 基于差分隐私的轨迹数据发布方法_林垚

### 基于停留点的差分隐私轨迹数据发布方法

- 停留点：在一段轨迹中，用户停留或不移动的时间超过阈值的地点

- 问题：停留点过多、停留点之间对用户的意义也不同（家、公司、商场、堵车点）

为解决以上问题，提出使用TF-IDF方法来根据停留点对用户的意义确定选择一定的停留点

#### TF-IDF

常用于爬虫、搜索引擎中，利用词频判断关联度等。

- 词频(Term Frequency)：指的是某一单词在一份文档中出现的频率； 
- 逆文本概率 (Inverse  Document Frequency)指的是某一单词出现过的文档数占文档总数的比例，它从侧面反映出该单词对文档的重要程度，逆文本概率越小，拥有该单词的文档就越具有区分度

在轨迹数据的停留点中对应：

- 词频对应：该停留点的停留时间占该轨迹中所有停留点的停留时间的比例，比例越高停留点意义越大
- 逆文本概率对应：存在该留点的轨迹数量占所有轨迹的比例，比例越低说明该停留点对此用户来说更加重要

![image-20211115201615944](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211115201615944.png)

$D$是轨迹的数据集，$T_d(S_i)$为停留点 $S_i$的停留时间。

#### 利用高斯机制，选择停留点并分配隐私预算

![image-20211115201914301](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211115201914301.png)

概率越高的停留点越容易被选择，对用于来说意义越大，被分配的隐私预算应该**越少**

#### 对停留点添加Laplace噪声

对二维噪声（角度和长度：极坐标）做一定约束：

- 角度在整体角度和最近一次角度之间
- 长度在最大移动距离之内（取余）

![image-20211115230252657](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211115230252657.png)



### 基于扩展卡尔曼滤波的差分隐私轨迹数据发布方法 

暂时不做研究

## 基于差分隐私的直方图发布算法研究_唐海霞

### 利用poisson分布（柏松）进行隐私预算的分配

泊松分布：离散型分布，概率密度函数如下：
$$
\Pr(X = i) = \frac{\lambda ^i} {i!} \mathrm{e} ^{-\lambda}
$$

$$
\sum_{i = 0}^{\infty} \frac{\lambda ^i} { i!} \mathrm{e} ^{-\lambda} = 1
$$

因此可以做到无限次数的隐私预算分配：
$$
\varepsilon_i = \frac{\lambda ^{i - 1}} { (i - 1)!} \mathrm{e} ^{-\lambda} \cdot \varepsilon
$$

#### 保证前k次的隐私预算分配

设置柏松分布：$X \sim P(k)$。

但是前$k$次的隐私预算和约为隐私预算的一般，没有做到把大部分的隐私预算分配在前k次。

基于，$\sum_{i=0}^{2 \lambda - 1} \dfrac{\lambda ^i} {i!} \mathrm{e} ^{-\lambda} \approx 1$，有以下的分配公式，：对于前 $k$ 次查询，我们用点$i$ 和点$i+k$ 的概率和作为隐私预算分配权重。

![image-20211116200238213](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211116200238213.png)



### 自适应差分隐私预算分配策略，重构误差和噪音误差的均衡问题

![image-20211116220444275](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211116220444275.png)

Laplace噪声的均方误差：$Lap(\dfrac{\Delta f}{\varepsilon})$
$$
\int_{-\infty}^{+\infty}x^2 \dfrac{1}{2b} \mathrm{e}^{-\frac{|x|}{b}} \mathrm{d}x = 2b^2, b = \frac{\Delta f}{\varepsilon}
$$
根据数据发布的均方误差：

![image-20211116215747721](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211116215747721.png)



对后两项（带有隐私预算分配权重 $k$ ）进行优化，计算取最小值时的$k$值：

![image-20211116215912804](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211116215912804.png)

利用自适应预分配 $\varepsilon-Partition(H)$，基于贪心思想：排序后顺序判断：

![image-20211116220411437](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211116220411437.png)

