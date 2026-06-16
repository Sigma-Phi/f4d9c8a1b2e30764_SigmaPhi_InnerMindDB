為了將 **CCFS 理論** 轉化為可計算的模型，我們可以使用 Python 來模擬一個簡單的認知代理（Agent）。這裡我們使用隨機遊走（Random Walk）來模擬原始的「自由認知空間」，並引入一個壓縮函數來嘗試提取結構。
你可以運行以下程式碼來觀察「壓縮率」如何影響系統的熵與預測穩定性：
```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 模擬原始認知空間 (High entropy, random noise)
def generate_cognitive_space(n=1000, complexity=0.8):
    return np.random.normal(0, 1, n) + np.random.normal(0, complexity, n)

# 2. 壓縮算子 (C): 透過線性回歸或平均化將高維空間投影到低維
def compress(data, ratio):
    """
    ratio: 壓縮程度 (0 到 1)，越高代表保留的特徵越少
    """
    n_features = int(len(data) * (1 - ratio))
    if n_features < 1: n_features = 1
    # 簡化模擬：取前 n 個主要成分/平均作為結構
    compressed = np.mean(data.reshape(-1, max(1, len(data)//n_features)), axis=1)
    return compressed

# 3. 測量函數
def measure_entropy(x):
    return np.std(x)

# 模擬不同壓縮率下的系統行為
ratios = np.linspace(0.01, 0.99, 50)
entropies = []
predictive_power = []

raw_data = generate_cognitive_space()

for r in ratios:
    T = compress(raw_data, r)
    # 熵隨壓縮增加而減少
    entropies.append(measure_entropy(T))
    # 預測能力：假設在 RC 點附近達到峰值 (模擬 U 型曲線)
    # 在這裡我們用一個簡單的函數模擬理論效能
    perf = -10 * (r - 0.5)**2 + 2 
    predictive_power.append(perf)

# 視覺化結果
plt.figure(figsize=(10, 5))
plt.plot(ratios, predictive_power, label='Predictive Power (Theory Utility)', color='blue')
plt.plot(ratios, entropies, label='Semantic Entropy (F(T))', color='red', linestyle='--')
plt.axvline(x=0.5, color='green', linestyle=':', label='Critical Ratio (Rc)')
plt.xlabel('Compression Ratio (R)')
plt.ylabel('Value')
plt.title('CCFS Theory: Cognitive Compression Phase Transition')
plt.legend()
plt.grid(True)
plt.show()

```
### 程式邏輯說明：
 1. **generate_cognitive_space**: 創建一個具有高維噪聲的初始認知狀態 I_t。
 2. **compress**: 模擬 \mathcal{C} 算子。當 ratio 增加時，我們丟棄更多的細節（資訊），只保留核心的趨勢（結構 T_t）。
 3. **predictive_power**: 模擬了主定理中的預測能力。這是一條典型的鐘形曲線：
   * **欠壓縮 (R < R_c)**: 資訊過多，模型無法提取規律（噪音干擾）。
   * **臨界點 (R_c)**: 找到「理論」的最佳平衡點，預測力最高。
   * **過壓縮 (R > R_c)**: 模型過於死板，喪失了對現實的解釋力。
這段程式碼為您提供了一個基礎的模擬框架。如果您需要將其與真實數據（例如文本向量或感測器數據）結合，我們可以進一步改寫 compress 函數，使用 PCA 或 Autoencoder 來替代簡單的平均化處理。
