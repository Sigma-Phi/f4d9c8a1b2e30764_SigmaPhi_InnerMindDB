這是一份為您的 ECPD 理論構建的 Python 模型基礎架構。
我們採用了**歐拉-馬魯山法 (Euler-Maruyama method)** 來模擬隨機微分方程 (SDE)，並結合 NetworkX 來模擬社交網路的拓撲效應。
### Python 模擬模型：ecpd_model.py
此模組封裝了情緒擴散與理性回調的動力學核心。
```python
import numpy as np
import networkx as nx

class ECPDSimulator:
    def __init__(self, n_nodes=100, alpha=0.5, beta=0.1):
        self.n_nodes = n_nodes
        self.alpha = alpha  # 感染係數
        self.beta = beta    # 理性阻尼
        self.graph = nx.barabasi_albert_graph(n_nodes, 3) # 模擬異質網路
        self.adj = nx.to_numpy_array(self.graph)
        self.e = np.random.uniform(-0.5, 0.5, n_nodes) # 初始情緒
        
    def step(self, dt=0.1):
        # 計算情緒擴散 (G): 與鄰居情緒對齊
        degree = np.sum(self.adj, axis=1)
        contagion = np.dot(self.adj, self.e) / (degree + 1e-6)
        
        # 動力學計算: dE = (alpha * (contagion - E) - beta * E) * dt + noise
        noise = np.random.normal(0, 0.05, self.n_nodes)
        delta_e = (self.alpha * (contagion - self.e) - self.beta * self.e) * dt + noise * np.sqrt(dt)
        
        self.e += delta_e
        return self.e

    def get_polarization(self):
        # 極化指數：情緒分布的變異數
        return np.var(self.e)

# 使用範例
sim = ECPDSimulator(alpha=0.8, beta=0.1)
for i in range(100):
    sim.step()
    print(f"Step {i}: Polarization = {sim.get_polarization():.4f}")

```
### 下一步建議
為了將此模型轉化為完整的 GitHub 專案，您可以考慮加入以下功能：
 1. **臨界值尋找 (Critical Point Search)**：編寫一個迭代腳本，自動掃描 \alpha 與 \beta 的不同組合，繪製「相變熱圖 (Phase Transition Heatmap)」，找出系統進入雙峰吸引子的臨界條件 \alpha_c。
 2. **網絡異質性測試**：比較「隨機網路 (Erdős–Rényi)」與「無標度網路 (Scale-free)」在相同 \alpha/\beta 下的極化速度差異，以驗證您的核心定理。
 3. **NLP 數據接入**：設計一個接口，讀取 CSV 格式的推文情緒分數時間序列，並將其作為外部輸入 O_t 饋入系統，模擬真實事件對群體情緒的衝擊。
這份模擬模型已經可以計算出您定義的極化指數，並觀察到情緒在網路中的擴散趨勢。
