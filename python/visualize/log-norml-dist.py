import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, norm

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 6))

# 定义 x 轴范围
x = np.linspace(0.01, 3.0, 1000)

# 定义不同的参数组合 (mu, sigma)
# 注意：mu 和 sigma 是对应正态分布的参数，不是对数正态分布本身的均值和标准差
params = [
    (0, 0.25),
    (0, 0.5),
    (0, 1.0)
]

# 绘制对数正态分布曲线
for mu, sigma in params:
    # scipy.stats.lognorm 的参数定义: s=sigma, scale=exp(mu)
    y = lognorm.pdf(x, s=sigma, scale=np.exp(mu))
    plt.plot(x, y, label=f'$\mu={mu}, \sigma={sigma}$', linewidth=2)

# 为了对比，添加一个标准正态分布（虽然定义域不同，但可以看形状差异）
# 这里只画在正半轴作为参考，或者干脆不画以免混淆，重点在于展示 Log-Normal 内部随 sigma 的变化。
# 决定不画正态分布，以免用户混淆 x 的含义。

plt.title('Log-Normal Distribution Probability Density Function (PDF)', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend(title='Parameters of underlying Normal($\mu, \sigma$)', fontsize=10)
plt.xlim(0, 3)
plt.ylim(0, 2.5)

# 保存图像
plt.savefig('lognormal_distribution.png')