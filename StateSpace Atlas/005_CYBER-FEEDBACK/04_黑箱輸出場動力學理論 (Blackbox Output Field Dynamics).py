import numpy as np
import matplotlib.pyplot as plt

def simulate_blackbox(steps=1000, alpha=0.3, beta=0.7):
    """
    黑箱輸出場動力學模擬器
    """
    input_tensions = np.linspace(0, 1, steps)
    latent_states = np.zeros(steps)
    outputs = np.zeros(steps)
    noise = np.random.normal(0, 0.05, steps)
    
    for t in range(1, steps):
        it = input_tensions[t]
        # 隱狀態演化方程: dX_t = F(Xt, Ot, Ut)dt + G(Xt, Ot, Ut)dW_t
        diffusion = 0.1 * it + noise[t]
        latent_states[t] = latent_states[t-1] + diffusion
            
        # 輸出穩定性映射
        if it < alpha:
            outputs[t] = 0.5 * it + np.random.normal(0, 0.01)
        elif alpha <= it < beta:
            # 高熵穩定區: 內部熵增加，輸出保持穩定
            outputs[t] = 0.5 * alpha + np.random.normal(0, 0.02)
        else:
            # 崩潰區: 映射失效
            outputs[t] = 0.5 * alpha + (it - beta) * 2 + np.random.normal(0, 0.1)
            
    return input_tensions, latent_states, outputs

# 執行與可視化
tensions, latents, outputs = simulate_blackbox()
# ... (繪圖代碼同上)
