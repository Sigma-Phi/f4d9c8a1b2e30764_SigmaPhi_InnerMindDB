import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# SCCD: Source-Controlled Cognitive Dynamics (Minimal Model)
# =========================================================

# -------------------------
# 1. Parameters
# -------------------------
T = 800                 # time steps
dt = 1.0

rho_S = 1.5             # source density (data pressure)
U = 1.2                 # control strength (regularization / governance)
noise_scale = 0.25      # stochastic disturbance

# -------------------------
# 2. State Initialization
# -------------------------
X = np.zeros(T)
X[0] = 0.1

# -------------------------
# 3. Drift Dynamics F(X, O, U)
# -------------------------
def drift(x, rho_S, U):
    """
    SCCD simplified dynamics:

    source term  -> expansion / entropy injection
    control term -> stabilization / compression
    """

    source_term = rho_S * np.tanh(x)
    control_term = -U * x

    return source_term + control_term


# -------------------------
# 4. Stochastic Term G dW
# -------------------------
def noise():
    return np.random.normal(0, noise_scale)


# -------------------------
# 5. Evolution Equation
# dX_t = F(X_t)dt + G dW
# -------------------------
for t in range(T - 1):
    dX = drift(X[t], rho_S, U) * dt + noise()
    X[t + 1] = X[t] + dX


# -------------------------
# 6. Stability Metric (Lyapunov-like)
# -------------------------
def stability_score(series):
    return np.var(series[-200:])  # late-stage variance

score = stability_score(X)

# -------------------------
# 7. Visualization
# -------------------------
plt.figure(figsize=(10, 4))
plt.plot(X, linewidth=1.5)
plt.title(f"SCCD Dynamics | ρ(S)={rho_S}, U={U}, Stability={score:.4f}")
plt.xlabel("Time")
plt.ylabel("Cognitive State X_t")
plt.grid(True)
plt.show()


# -------------------------
# 8. Phase Transition Sweep
# -------------------------
rho_vals = np.linspace(0.2, 3.0, 25)
U_vals = np.linspace(0.2, 3.0, 25)

heatmap = np.zeros((len(rho_vals), len(U_vals)))

def simulate(rho_S, U):
    x = 0.1
    traj = []

    for _ in range(250):
        x = x + rho_S * np.tanh(x) - U * x + np.random.normal(0, 0.2)
        traj.append(x)

    return np.var(traj[-100:])

for i, r in enumerate(rho_vals):
    for j, u in enumerate(U_vals):
        heatmap[i, j] = simulate(r, u)

plt.figure(figsize=(6, 5))
plt.imshow(heatmap, origin="lower", cmap="viridis")
plt.colorbar(label="Instability (Variance)")
plt.xlabel("Control U")
plt.ylabel("Source ρ(S)")
plt.title("SCCD Phase Transition Map")
plt.show()
