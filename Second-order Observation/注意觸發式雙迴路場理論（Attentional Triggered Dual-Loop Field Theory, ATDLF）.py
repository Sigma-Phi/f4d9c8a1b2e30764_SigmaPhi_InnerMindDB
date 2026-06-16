為了將「注意觸發式雙迴路場理論（ATDLF）」轉化為可運行的 Python 模擬程式，我們可以使用 scipy.integrate.solve_ivp 來處理隨機微分方程（SDE）的數值近似。
這裡提供一個基礎的 **Euler-Maruyama 求解器架構**，模擬系統在注意門控下的狀態軌跡。
### ATDLF 理論模擬器 (Python)
```python
import numpy as np
import matplotlib.pyplot as plt

def atdlf_simulation(steps=1000, dt=0.01):
    # 狀態變數: X_t (2D 向量)
    X = np.zeros((steps, 2))
    X[0] = [1.0, 1.0] # 初始狀態
    
    # 紀錄指標
    A_log = []
    T_log = []
    
    # 參數設置
    tau_r = 0.8  # 重構閾值
    
    for t in range(1, steps):
        # 1. 計算注意場 (模擬與目標的誤差作為注意強度)
        error = np.linalg.norm(X[t-1])
        A_t = np.tanh(error) # 注意力隨誤差非線性增加
        
        # 2. 計算觸發事件
        T_t = np.random.rand() * (error / 2) # 簡化觸發模型
        
        # 3. 定義雙迴路動力
        # Fc: 修正流 (傾向回到原點)
        F_c = -0.5 * X[t-1]
        # Fr: 重構流 (若 T_t > tau_r 則產生擾動)
        F_r = np.array([0.5, -0.5]) if T_t > tau_r else np.array([0.0, 0.0])
        
        # 4. 隨機項 (dW)
        dW = np.random.normal(0, np.sqrt(dt), 2)
        
        # 5. 更新狀態
        dX = A_t * (F_c + F_r) * dt + 0.1 * dW
        X[t] = X[t-1] + dX
        
        A_log.append(A_t)
        T_log.append(T_t)
        
    return X, A_log, T_log

# 執行模擬
X, A, T = atdlf_simulation()

# 繪製結果
plt.figure(figsize=(10, 5))
plt.plot(X[:, 0], X[:, 1], label='State Trajectory')
plt.title("ATDLF System Trajectory")
plt.xlabel("X1"); plt.ylabel("X2")
plt.grid(True)
plt.show()

```
### 理論到程式的實現關鍵點
為了讓這段程式碼更貼近您的數學模型，建議在後續開發中引入以下邏輯：
 1. **非線性函數 (F_c, F_r) 的具體化**：
   目前的 F_c 是簡單的線性回歸，若要模擬複雜系統，建議將其替換為神經網路（如 torch.nn.Linear）或非線性吸引子方程（如 Lorenz 吸引子），以體現 Correction 的動態。
 2. **重構的塑性 (Plasticity)**：
   在 F_r 的邏輯中，您可以增加一個 Weights 矩陣的更新步驟。這意味著當 T_t > \tau_r 時，不僅狀態 X_t 改變，連帶控制策略 F_c 的參數也會發生演化。
 3. **臨界減速檢測**：
   可以在循環中加入一個「滑動窗口」來計算 dX_t/dt 的方差。當接近 \tau_r 時，方差的變化率會下降，這就是您理論中預測的「臨界減速」現象。
這個 Python 架構為您提供了一個實驗平台，您可以透過調整 tau_r 和 A_t 的靈敏度，觀察系統何時從「穩定修正」切換到「劇烈重構」。
