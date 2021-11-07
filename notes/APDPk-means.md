# APDPk-means

APDPk-means: A new differential privacy clustering algorithm based on arithmetic progression privacy budget allocation

通俗来讲就是把总体的隐私预算作为一个等差数列和，把最小隐私预算作第一项，以最大迭代数为项数，计算等差数列。最后将等差数列逆序为一个降序的等差数列作为一个隐私分类的序列。

## K-means

K-Means 是一种非常简单的聚类算法(聚类算法都属于无监督学习)。给定固定数量的聚类和输入数据集，该算法试图将数据划分为聚类，使得聚类内部具有较高的相似性，聚类与聚类之间具有较低的相似性。

k维数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$，算法将数据集中的数据分为k个聚类 $C=\{C_1,C_2,\ldots,C_k\}$，并且使得the sum of squared errors(SSE)最小。
$$
SSE=\sum_{i=1}^{k} \sum_{x \in C_i} ||x-\mu_i||_2
$$

$$
\mu_i = \frac{1}{|C_i|} \sum_{x \in C_i} x
$$



### Algorithm

输入：数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$，聚类的簇数$k$，最大迭代次数$N$

输出：簇划分 $C=\{C_1,C_2,\ldots,C_k\}$

- 从数据集$D$中随机选择$k$个样本作为初始的$k$个质心向量： $\{μ_1,μ_2,...,μ_k\}$
- 将样本 $x_i$分类到$C=\{C_1,C_2,\ldots,C_k\}$中，（寻找距离 $x_i$最近的 $\mu_i$）
- 使用公式2，对每个聚类 $C_j$重新计算质心
- 重复2、3步骤，知道到达最大迭代次数，或聚类划分不再改变

### K-means Problem

在初始点的选择和质点更新计算的过程（$\mu_i = \frac{1}{|C_i|} \sum_{x \in C_i} x$，实际上对某一聚类的统计查询）中会导致隐私的泄漏。

因此在K-means聚类算法中加入差分隐私的机制。主要思想是在进行初始点的选择和质点更新计算的过程中添加Laplace噪声。因此引入DPK-means。

## DPK-means

### Algorithm

输入：数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$，聚类的簇数$k$，最大迭代次数$N$

输出：簇划分 $C=\{C_1,C_2,\ldots,C_k\}$

- 初始化数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$到 $[0,1]^d$区间，在其中选取$k$个样本 $\{μ_1,μ_2,...,μ_k\}$，加入噪声后 $\{μ_1',μ_2',...,μ_k'\}$作为初始质心
- 将样本 $x_i$分类到$C=\{C_1,C_2,\ldots,C_k\}$中，（寻找距离 $x_i$最近的 $\mu_i'$）
- 对每个聚类样本 $C_j$，计算$sum$和$num$，添加噪声后为$sum'$和$num'$，基于公式2，计算新的质心 $\mu_j''=sum'/num'$
- 重复2、3步骤，知道到达最大迭代次数，或聚类划分不再改变

## Pricvacy budget allocation

在一个质心的更新过程中，实际上是一个分割d-dimensional space的直方图查询。因此可以考虑在整个聚类算法算法中的查询敏感度为 $d+1$。
$$
\Delta f=d+1
$$

### Uniform allocation 统一分配

在已知迭代次数$N$的情况下，每次更新质心的隐私预算为 $\varepsilon /N$，（整个算法的隐私预算为 $\varepsilon$）。因此每一轮添加的Laplace噪声为 $Lap((d+1)N/\varepsilon)$。

### Dichotomy allocation 二分法分配/指数

在未知迭代次数$N$的情况下，首次更新质心的隐私预算为 $\varepsilon /2$，之后每次更新质心的隐私预算为上一轮的 $1/2$。$\varepsilon _i = \varepsilon / 2^i$

### Series sum allocation 序列和分配

根据 $\sum_{i=1}^{\infty} 1/i(i+1)=1$，所以第 $i$轮迭代的隐私预算为 $\varepsilon_i=\varepsilon/i(i+1)$，添加的Laplace噪声为 $Lap((d+1)i(i+1)/\varepsilon)$。



## APDPk-means

### Arithmetic progressions allocation 算术级数隐私预算分配

该方法的主要思想是将总隐私预算分解为递减的算术级数，在迭代过程中从大到小分配隐私预算。

算术级数的递减分配隐私预算可以保证在早期迭代中快速收敛。

一些性质：

- 总的隐私预算越小，每两轮之间的隐私预算差值就越小
- 当总的隐私预算小于最小隐私预算 $\varepsilon^m$（公式4），添加的噪声会影响质心的更新，因此APDPk-means就退化为统一分配。

$$
\varepsilon^m=\left(\frac{500k^3}{N^2}\left(d + \sqrt[3]{4d \rho ^2 } \right)^3\right) ^{1/2}
$$

其中$N$是数据集大小（数据记录条数），$d$是数据的维度，$k$是聚类的个数，$\rho$是聚类质心的第$i$维的归一化坐标，$\rho=sum/2r(num)$。当坐标被归一化到 $[0,1]$上时，$\rho$被优化为0.45。

算术级数（等差数列）隐私预算计算公式：
$$
\varepsilon = \left(\varepsilon^m + \varepsilon'\right)n/2
$$

$$
\varepsilon_i = \varepsilon^m + (i-1)d 
$$

$$
d = 2\left(\varepsilon - n\varepsilon^m \right)/n\left(n-1\right)
$$



### Algorithm

使用算术级数隐私预算分配，并在优化了第一步的初始质心随机化，提高可用性

输入：数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$，聚类的簇数$k$，总体的隐私预算 $\varepsilon$，最大迭代次数$t_m$

输出：簇划分 $C=\{C_1,C_2,\ldots,C_k\}$

- 初始化数据集 $D=\{x_1, x_2,⸱⸱⸱, x_n\}$到 $[0,1]^d$区间，并把数据集D均匀分为$k$ 个互斥的子集$S=\{S_1,S_2,\ldots,S_k\}$
- 对这$k$个子集，在其中随机选其一个样本$o_i$，并对他们加上噪声变为 $\{\mu_1,\mu_2,\ldots,\mu_k\}，作为初始质心
- 计算隐私预算序列
  - 如果 $\varepsilon/\varepsilon^m > t_m$，则利用公式5，6，7计算算术级数隐私预算
  - 否则，退化为统一分配，$\varepsilon_i = \varepsilon/t_m$
- 将样本 $x_i$分类到$C=\{C_1,C_2,\ldots,C_k\}$中，（寻找距离 $x_i$最近的 $\mu_i'$）
- 对每个聚类样本 $C_j$，计算$sum$和$num$，添加噪声（$Lap((d+1)/\varepsilon_i)$）后为$sum'$和$num'$，基于公式2，计算新的质心 $\mu_j''=sum'/num'$
- 重复4、5步骤，知道到达最大迭代次数，或聚类划分不再改变

