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

# [2 Differential Privacy 概念介绍](https://zhuanlan.zhihu.com/p/61179516)

### 概念

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

