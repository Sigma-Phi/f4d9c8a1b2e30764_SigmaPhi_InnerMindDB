我們可以使用隨機微分方程（SDE）的數值解法（如歐拉-丸山法，Euler-Maruyama Method）。
以下是該模型的 Python 實現，並展示了系統如何在持續擾動下，受限於「有界動態穩態吸引子」的行為。
### Python 計算模型代碼
```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_edd(steps=1000, dt=0.01, alpha=0.5, sigma=0.2):
    """
    實現平衡漂移動力學的離散時間模擬
    公式: dX_t = -alpha * X_t * dt + sigma * dW_t
    - alpha: 回返效率 (R_t)，將系統拉回中心的係數
    - sigma: 漂移強度 (D_t)，隨機擾動的標準差
    """
    X = np.zeros(steps)
    # 產生隨機擾動 (Gaussian White Noise)
    dW = np.random.normal(0, np.sqrt(dt), steps)
    
    for t in range(1, steps):
        # 演化方程: 修正行為 + 隨機擾動
        X[t] = X[t-1] - (alpha * X[t-1] * dt) + (sigma * dW[t])
        
    return X

# 參數設定
steps = 1000
alpha_val = 0.5  # 較高的回返效率
sigma_val = 0.3  # 擾動強度

# 執行計算
drift_data = simulate_edd(steps, alpha=alpha_val, sigma=sigma_val)

# 顯示計算結果
plt.figure(figsize=(10, 5))
plt.plot(drift_data, color='teal', linewidth=1, label='System State $X_t$')
plt.axhline(0, color='red', linestyle='--', alpha=0.6, label='Equilibrium Center $X^*$')
plt.title(f'Equilibrium Drift Dynamics (alpha={alpha_val}, sigma={sigma_val})')
plt.legend()
plt.show()

```
### 模型的設計說明
 1. **控制律建模 (U_t = -\alpha X_t)**：
   我們將回返效率 R_t 簡化為比例控制係數 \alpha。當 \alpha 越大，系統回到零點的速度越快。這精確反映了您定義中「將偏差轉換為修正行為」的能力。
 2. **擾動項 (G \cdot dW_t)**：
   透過 np.random.normal 生成布朗運動增量 dW_t。這代表了系統外部的隨機性，保證了系統永遠不會「靜止」在零點，而是呈現一種在零點附近震盪的漂移狀態。
 3. **邊界穩態 (Bounded Attractor)**：
   模型計算結果清楚顯示，系統狀態 X_t 不會單調發散，也不會收斂到一個點，而是始終被「囚禁」在一個由 \sigma 和 \alpha 共同決定的區間內，這正是您理論中所述的**有界動態穩態吸引子**。
### 接下來的計算擴展建議
如果您希望進一步深化此模型，我可以協助您增加以下複雜度：
 * **延遲效應**：引入 X_{t-\tau}，模擬修正過程中的滯後，觀察系統如何從「穩態區」轉移到「混沌區」。
 * **非線性修正**：將 - \alpha X_t 改為更複雜的非線性函數（如 Logistic 成長或飽和控制），以模擬更真實的生物或社會系統邊界條件。
