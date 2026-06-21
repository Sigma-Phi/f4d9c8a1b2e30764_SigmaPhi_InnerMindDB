這是一個「同態穩態動力系統論」(Homeostatic Isomorphic Dynamical Systems Theory) 轉化為可計算模型的 Python 實作。
此程式碼使用 numpy 進行數值模擬，透過歐拉-馬力亞馬法 (Euler-Maruyama method) 求解隨機微分方程，並視覺化系統在不同擾動強度下的狀態演變。
```python
import numpy as np
import matplotlib.pyplot as plt

class HomeostaticSystem:
    """
    同態穩態動力系統模型 (Homeostatic Isomorphic Dynamical System)
    dX_t = (kappa * (X_target - X_t) + U_t) * dt + sigma * dW_t
    """
    def __init__(self, kappa=0.5, X_target=1.0, sigma=0.1):
        self.kappa = kappa        # 恢復速率 (Recovery rate)
        self.X_target = X_target  # 理想同態目標
        self.sigma = sigma        # 隨機擾動強度

    def simulate(self, T=100, dt=0.01, perturbation_func=None):
        n = int(T / dt)
        t = np.linspace(0, T, n)
        X = np.zeros(n)
        X[0] = self.X_target
        
        for i in range(1, n):
            # 外部擾動 O_t
            O_t = perturbation_func(t[i]) if perturbation_func else 0
            
            # 修正控制 U_t (假設 U_t 對抗 O_t 的偏移)
            U_t = -0.5 * O_t 
            
            # 系統演化 dX_t
            drift = self.kappa * (self.X_target - X[i-1]) + U_t - O_t
            diffusion = self.sigma * np.random.normal(0, np.sqrt(dt))
            
            X[i] = X[i-1] + drift * dt + diffusion
            
        return t, X

# --- 模擬情境設定 ---
# 設置一個隨時間增加的擾動 O_t
def external_forcing(t):
    # 模擬從低擾動到臨界點的壓力
    return 0.1 * t if t < 50 else 5.0 

model = HomeostaticSystem(kappa=0.8, X_target=1.0)
t, X = model.simulate(T=100, perturbation_func=external_forcing)

# --- 視覺化 ---
plt.figure(figsize=(10, 5))
plt.plot(t, X, label='Isomorphic Coherence (X_t)')
plt.axhline(y=1.0, color='r', linestyle='--', label='Ideal State (X*)')
plt.title('Homeostatic Isomorphic Dynamical System Evolution')
plt.xlabel('Time (t)')
plt.ylabel('Coherence Degree (X_t)')
plt.legend()
plt.grid(True)
plt.show()

```
### 模型說明：
 1. **隨機微分方程 (SDE) 核心**：程式中的 drift 項結合了恢復力 \kappa(X^* - X_t) 與控制力 U_t，反映了系統對於擾動 O_t 的抵抗與適應。
 2. **擴散項 (Diffusion)**：使用 dW_t 來模擬環境隨機漲落，展示系統在穩態下的微觀波動。
 3. **可擴展性**：
   * 若要測試 **VI. Lyapunov 穩定性**，您可以修改 kappa 參數並觀察 V(X_t) = \|X_t - X^*\|^2 的下降趨勢。
   * 若要測試 **VIII. 可證偽預測**，可以將 kappa 設定為極小值，觀察系統是否無法收斂回 X^*。
