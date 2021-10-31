# Papers Notes

## [1 差分隐私保护：从入门到脱坑](https://www.freebuf.com/articles/database/182906.html)

### 概念

**差分隐私（Differential Privacy）是密码学中的一种手段，旨在提供一种当从统计数据库查询时，最大化数据查询的准确性，同时最大限度减少识别其记录的机会。简单地说，就是在保留统计学特征的前提下去除个体特征以保护用户隐私。**

差分隐私可以分为两种：中心化差分隐私和本地化差分隐私

中心化的差分隐私方法，引出了主流的拉普拉斯机制和指数机制。

在本地化差分隐私中，由于没有全局敏感度的概念，因此拉普拉斯机制和指数机制不再适用，大多数方案采用随机响应机制。

算法M通过对输出结果的随机化来提供隐私保护，同时通过参数ε来保证在数据集中删除任一记录时，**算法输出统一结果的概率不发生显著变化。**

![](https://image.3001.net/images/20180902/1535870884_5b8b87a4174c6.png!small)

### DP组合性质

#### **性质1**

假设有n个随机算法K，其中Ki满足εi-差分隐私，则{Ki}（1<=i<=n）组合后的算法满足sum(εi)-差分隐私。

#### **性质2**

设有n个随机算法K，其中Ki满足εi-差分隐私，且任意两个算法的操作数没有交集，则{Ki}（1<=i<=n）组合后的算法满足max(εi)-差分隐私。

## [2 Differential Privacy 概念介绍](https://zhuanlan.zhihu.com/p/61179516)

### 概念

**保护数据隐私的方法就是将原有的单一查询结果概率化**

背景知识攻击：**假定敌手拥有除了当前我拥有的数据之外的所有其他知识**。

**在保证数据可用的前提下，尽可能少地泄露隐私。**

**如果对相邻数据集的查询结果越像，那么隐私保护力度越大！**

![image-20211030102800609](https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211030102800609.png)



1. (x,y)是无序的，我们用概率**比值**来衡量相似程度
2. 相邻数据集意味着对每一条记录都提供保护

### Coin Flipping应用

（1）扔一枚硬币，如果正面朝上，老实回答自己是否抽烟
（2）如果反面朝上，则重复扔一枚硬币，如果正面朝上就回答“抽烟”，反面朝上就回答“不抽烟”。

#### 有效性

用 ![[公式]](https://www.zhihu.com/equation?tex=p_a) 表示被调查者抽烟的概率（即我们想获得的结果），用 ![[公式]](https://www.zhihu.com/equation?tex=p_b) 表示我们收集到的抽烟人数的比例，则根据上面的过程有：

![[公式]](https://www.zhihu.com/equation?tex=p_b+%3D+0.5p_a%2B0.25)

因此： ![[公式]](https://www.zhihu.com/equation?tex=Pa%3D2Pb%E2%88%920.5) 。所以根据统计的 ![[公式]](https://www.zhihu.com/equation?tex=p_b) 可以估计出 ![[公式]](https://www.zhihu.com/equation?tex=p_a) ，这个估计人群吸烟比例的方法是正确的（假设有足够多的样本）。

#### 隐私性

P[‘抽烟’ | ‘抽烟’] = 0.75
P[‘抽烟’ | ‘不抽烟’] = 0.25
P[‘不抽烟’ | ‘不抽烟’] = 0.75
P[‘不抽烟’ | ‘抽烟’] = 0.25

![](https://pic4.zhimg.com/80/v2-68cc85e20633eebd85e45b7903152fa3_1440w.png)

计算可得ϵ=ln3，所以我们说 Coin Flipping 机制是提供了ln3-DP的。

## [3 Differential Privacy 简介](https://zhuanlan.zhihu.com/p/139114240)

### 严格差分隐私定义

严格差分隐私

![v2-df71f363007b1d302d464d8d56852bd1_1440w](https://raw.githubusercontent.com/Jechin/PicLib/main/image/v2-df71f363007b1d302d464d8d56852bd1_1440w.png)

### [KL散度](https://zhuanlan.zhihu.com/p/95687720)

引入KL散度来描述两种分布之间的差异，以此来描述相邻数据集之间的差异（信息熵的损失）

KL散度的由来在4 瑞丽熵和瑞丽散度中指出
$$
D_{KL}(p||q) = \sum_{i=1}^Np(x_i)\cdot (\log p(x_i)-\log q(x_i))
$$
但是我们并不关心这两个分布的整体差异（期望），我们只需要两个分布在差距最大的情况下能够被bound住，所以引入了`MAX-Divergence`，并且使得它小于$\varepsilon$ :

![](https://pic4.zhimg.com/80/v2-68cc85e20633eebd85e45b7903152fa3_1440w.png)

其中$\varepsilon$被称为隐私预算，一般而言，$\varepsilon$越小，隐私保护越好，但是加入的噪声就越大，数据可用性就下降了。

**对于应用差分隐私的算法，首先会设定整体的隐私预算，每访问一次数据，就会扣除一些预算，当预算用完，数据就无法再访问。？？**

### 宽松差分隐私

引入delta

![](https://pic1.zhimg.com/80/v2-54d707ee5f7eb6e1b4dc64f20853fe6c_1440w.png)

对应的`Max-Divergence`

![](https://pic3.zhimg.com/80/v2-8232f370700aaa3e20ea09b1ea65c2ba_1440w.png)

## [4 瑞丽熵和Renyi Divergence(瑞丽散度)](https://zhuanlan.zhihu.com/p/140945752)

### Renyi Entropy瑞丽熵

$$
\H _{\alpha}(X) = \frac{1}{1-\alpha}\log(\sum_{i=1}^n p_i^{\alpha}), \alpha \ge 0,\alpha \ne 1X
$$

$\alpha = 0$, $\H_0(X) = \log n$为`Hartley熵`

$\alpha  \to 1$, $\H _1(X) = -\sum_{i=1}^n p_i \ln p_i$ ,为`香农熵`

$\alpha \to \infty $,  $\H_{\infty}(X) = -\log \max_i p_i$, 为`min-entropy`,最小熵

### Renyi Divergence瑞丽散度

瑞丽散度不表示距离（不满足对称性）但是可以表示分布的差距
$$
D_{\alpha}(P||Q) = \frac{1}{\alpha -1}\log(\sum_{i=1}^{n}q_i\frac{p_i^{\alpha}}{q_i^{\alpha}})
$$
$\alpha \to 1$, $D_1(P||Q) = \sum_{i=1}^np_i\log \frac{p_i}{q_i}$, 为 `KL-Divergence`

$\alpha \to \infty$, $D_{\infty}(P||Q) = \log \max \frac{p_i}{q_i}$, 为`max-Divergence`

### Differential Privacy Divergence

使用`max-devergence`进行 $\varepsilon$约束，得到 $\varepsilon$-差分隐私
$$
D_{\infty}(P||Q) = \log \max_i \frac{p_i}{q_i} \le \varepsilon
$$
**宽松差分隐私的的隐私预算以及有限的alpha（未理解）**

<img src="https://raw.githubusercontent.com/Jechin/PicLib/main/image/image-20211030220404943.png" alt="image-20211030220404943" style="zoom:50%;" />

## [5 Laplace Mechanism](https://zhuanlan.zhihu.com/p/64332308)

**保护数据隐私的方法就是将原有的单一查询结果概率化**，在查询结果中加上均值为0的Laplace噪声。

尽管噪声的均值为0，但是噪声的大小在设计中也起到一定作用。因此，如何设计DP机制和查询也是紧密相关的。

Laplaceti提供严格的 $(\varepsilon ,0)-DP$，$\delta=0$。松弛项为0。

### 查询敏感度 L1 Sensitivity

定义了**L1-Sensitivity**，一范式（绝对值之和）来表示f查询下相邻数据集之间查询结果的最大差异。

![[公式]](https://www.zhihu.com/equation?tex=f%3A%5Cmathbb%7BN%7D%5E%7B%5Cmathcal%7B%7CX%7C%7D%7D%5Crightarrow+%5Cmathbb%7BR%7D%5Ek)

![equation](https://raw.githubusercontent.com/Jechin/PicLib/main/image/equation.svg)

### Laplace分布

Laplace分布的概率密度函数：

![](https://www.zhihu.com/equation?tex=f%28x%7C%5Cmu%2Cb%29%3D%5Cfrac%7B1%7D%7B2b%7D%5Cexp+%28-%5Cfrac%7B%7Cx-%5Cmu%7C%7D%7Bb%7D%29%3D%5Cfrac%7B1%7D%7B2b%7D%5Cbegin%7Bcases%7D+%5Cexp%28-+%5Cfrac%7B%5Cmu-x%7D%7Bb%7D%29+%26+x+%3C+%5Cmu+%5C%5C+%5Cexp%28-+%5Cfrac%7Bx-%5Cmu%7D%7Bb%7D%29+%26+x+%5Cge+%5Cmu+%5Cend%7Bcases%7D%5C%5C)

### Laplace-DP机制

$$
M(D) = f(D) + Y \\
Y \sim L(0, \frac{\Delta f}{\varepsilon})
$$

满足 $(\varepsilon,0)-DP$

### Laplace应用（数值型查询）

1. Counting Queries统计查询，查询敏感度为1，加上 $L(0,1/\varepsilon)$的噪声
2. Histogram Queries直方图查询，查询敏感度为1，加上 $L(0,1/\varepsilon)$的噪声



## [6 Gaussian Mechanism](https://zhuanlan.zhihu.com/p/144318152)	

Gaussian提供宽松松弛的差分隐私

### 查询敏感度 L2 Sensitivity

定义L2-Sensitivity，二范式（欧几里得范数，绝对值的平方和再开方）

![L2-Sensitivity](https://pic1.zhimg.com/80/v2-cb21e86ceab20ba8b3664cb3a8823774_1440w.png)

### 正态分布

GDP添加正态分布的噪声。 

正态分布的概率密度函数如下：
$$
f(x)=\frac{1}{\sqrt{{2\pi}}\sigma}
\exp(\frac{(x-\mu)^2}{2\sigma^2})
$$
$(\varepsilon , \delta)-DP$满足如下
$$
\Pr [M(D) \in S] \le e^{\varepsilon} \Pr [M(D') \in S] + \delta \\
M(D) = f(D) + Y \\
Y \sim \mathcal N (0, \sigma ^2), \sigma > \frac{\sqrt{s \ln(1.25/\delta)}\Delta f}{\varepsilon}
$$


### Gaussian Mechanism应用于数值型查询

### Gaussian-DP证明

1. 在松弛差分隐私中，输出可以分为两部分，一部分是严格遵守差分隐私的，另一部分是违反了严格差分隐私的。
2. 因此我们需要将输出集合分隔成两部分，证明第一部分是被 $\varepsilon$ 约束住，而第二部分小于 $\delta$ 。

## [7 Exponential Mechanism](https://zhuanlan.zhihu.com/p/144318152)

指数机制针对于非数值型的查询，查询结果为一组离散数据中 $\{R_1, R_2,\ldots, R_N\}$ 的一项

整体思想为：将确定的查询结果转变为按一定概率输出在离散数据中的不确定输出。在离散数据中每一项针对这一查询的输出概率由打分函数$\mu$决定，分数越高，概率越高。

### 打分函数

定义一个打分函数为$q$，其中$N^{|\mathcal X|}$为多维数据集，$\mathcal R$为一组结果离散集，查询的结果为$\mathcal R$中的一项，$\R$为实数集。
$$
q: \N^{|\mathcal X|} \times \mathcal R \to \R
$$

### 查询敏感度 L1 Sensitivity

$$
\Delta q = \max_{D,D'} ||q(D,R_i)-q(D',R_i)||_1
$$

### 分布

Exponential Mechanism指数机制以 $M(D,q,R_i) \sim \exp(\frac{\varepsilon q(D, R_i)}{2 \Delta q})$ （正比于）的概率输出结果。

归一化为概率后：
$$
\Pr[R_i] = \frac{\exp(\frac{\varepsilon q(D, R_i)}{2 \Delta q})}
{\sum_{R_j \in \mathcal R} \exp(\frac{\varepsilon q(D, R_j)}{2 \Delta q})}
$$
**隐私预算和可用性成正比，和隐私保护成反比。**

### Exponential Mechanism应用于非数值型的查询





