import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# 1. Generate negative linearly correlated data
# 生成负线性相关数据
# Slope ~ -1.5
x = np.linspace(0, 3, 100) # Reduced range slightly to keep points visible
slope = -1.5
intercept = 4.5 # Adjusted intercept to keep y values in a range that shows the decay well (approx 4.5 to 0)
noise = np.random.normal(0, 0.2, size=len(x))
y = slope * x + intercept + noise

# 2. Apply exponential transformation
# 对所有数据取指数
x_exp = np.exp(x)
y_exp = np.exp(y)

# 3. Plotting
plt.figure(figsize=(12, 5))

# Plot 1: Original Negative Linear Data
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points')
plt.plot(x, slope * x + intercept, color='red', linestyle='--', label=f'True Line: y={slope}x+{intercept}')
plt.title('Original Data (Negative Linear Correlation)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Plot 2: Exponentially Transformed Data
plt.subplot(1, 2, 2)
plt.scatter(x_exp, y_exp, color='purple', alpha=0.7, label='Transformed Points')
plt.title('Exponential Transformed Data ($e^x$ vs $e^y$)')
plt.xlabel('$e^x$')
plt.ylabel('$e^y$')

# Add theoretical trend line
# Y = e^(mx+c) = e^c * X^m
# Here m = -1.5, so Y proportional to X^(-1.5) -> Decay curve
X_smooth = np.linspace(np.min(x_exp), np.max(x_exp), 100)
Y_smooth = np.exp(intercept) * (X_smooth ** slope)
plt.plot(X_smooth, Y_smooth, color='green', linestyle='--', label=f'Power Law: $Y \\propto X^{{{slope}}}$')

plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('negative_linear_vs_exponential.png')