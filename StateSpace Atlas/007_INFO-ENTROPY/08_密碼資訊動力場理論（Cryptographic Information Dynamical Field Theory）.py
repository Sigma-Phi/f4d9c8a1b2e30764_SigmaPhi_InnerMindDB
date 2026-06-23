# -*- coding: utf-8 -*-
"""
Cryptographic Information Dynamical Field Theory
→ 可計算模型 (Computational Model Prototype)

將「密碼資訊動力場理論」轉換為可模擬的多代理 + 隨機動力系統框架
"""

import numpy as np

# =========================
# 1. 系統參數
# =========================

class Params:
    def __init__(self):
        # control parameters
        self.alpha = 0.6   # control density
        self.beta = 0.5    # transaction flux

        # cryptographic potential scaling
        self.crypto_strength = 0.8

        # noise intensity
        self.sigma = 0.1

        # system size (agents / nodes)
        self.N = 50


# =========================
# 2. 系統狀態 X_t
# =========================
# X_t[i] = agent i 的「可見性狀態」
# 範圍: 0 (不可見) ~ 1 (完全可見)

class SystemState:
    def __init__(self, N):
        self.X = np.random.rand(N)


# =========================
# 3. 核心動力學 F(X, O, U)
# =========================

def compute_F(X, params):
    """
    deterministic drift:
    - control pulls system toward structured visibility
    - crypto pushes toward invisibility
    - transaction pushes toward homogenization
    """

    N = len(X)
    F = np.zeros(N)

    mean_X = np.mean(X)

    for i in range(N):

        # 密碼勢能 → 壓低可見性
        crypto_force = -params.crypto_strength * X[i]

        # 控制場 → 向結構均值對齊（集中化）
        control_force = params.alpha * (mean_X - X[i])

        # 交易流 → 增加混合與擴散
        transaction_force = params.beta * (np.random.rand() - X[i])

        F[i] = crypto_force + control_force + transaction_force

    return F


# =========================
# 4. 隨機擾動 G dW
# =========================

def compute_noise(X, params):
    return params.sigma * np.random.randn(len(X))


# =========================
# 5. 系統更新 (Euler-Maruyama)
# =========================

def step(X, params, dt=0.01):
    F = compute_F(X, params)
    noise = compute_noise(X, params)

    X_new = X + F * dt + noise * np.sqrt(dt)

    # 限制在 [0,1]
    X_new = np.clip(X_new, 0.0, 1.0)

    return X_new


# =========================
# 6. 可見熵（Visibility Entropy）
# =========================

def visibility_entropy(X, bins=10):
    hist, _ = np.histogram(X, bins=bins, density=True)
    hist = hist + 1e-12
    return -np.sum(hist * np.log(hist))


# =========================
# 7. Lyapunov-like function
# =========================

def lyapunov(X):
    return np.var(X) + (np.mean(X) - 0.5) ** 2


# =========================
# 8. 模擬主程式
# =========================

def simulate(T=200, dt=0.01):
    params = Params()
    state = SystemState(params.N)

    history_entropy = []
    history_lyap = []

    X = state.X

    for t in range(T):

        # 更新系統
        for _ in range(int(1/dt)):
            X = step(X, params, dt)

        # 記錄
        history_entropy.append(visibility_entropy(X))
        history_lyap.append(lyapunov(X))

    return X, history_entropy, history_lyap


# =========================
# 9. 相變檢測（簡化版）
# =========================

def detect_phase(X, params):
    mean_X = np.mean(X)
    entropy = visibility_entropy(X)

    if entropy < 1.0 and params.crypto_strength > 0.7:
        return "Cryptographic Stability (加密穩定態)"

    elif params.alpha > 0.8:
        return "Control Lockdown (控制鎖定態)"

    elif params.beta > 0.7:
        return "Economic Diffusion (經濟滲透態)"

    elif mean_X < 0.2:
        return "Collapse (崩解態)"

    else:
        return "Open Flow (開放流動態)"


# =========================
# 10. 執行示例
# =========================

if __name__ == "__main__":
    X_final, entropy_hist, lyap_hist = simulate()

    params = Params()
    phase = detect_phase(X_final, params)

    print("Final Phase:", phase)
    print("Final Mean Visibility:", np.mean(X_final))
    print("Final Entropy:", entropy_hist[-1])
