import numpy as np

class BayesianControlDynamicalSystem:
    """
    Discrete-time approximation of:
    dX_t = F(X_t, O_t, U_t)dt + G(X_t, O_t, U_t)dW_t
    """

    def __init__(
        self,
        dim=1,
        alpha=0.5,   # control strength
        beta=0.3,    # noise strength
        lr=0.1,      # belief update rate
        seed=42
    ):
        self.dim = dim
        self.alpha = alpha
        self.beta = beta
        self.lr = lr

        np.random.seed(seed)

        # belief state X_t (internal estimate)
        self.X = np.zeros(dim)

        # latent "true world state" (unknown to agent)
        self.true_state = np.random.randn(dim)

    # ----------------------------
    # Observation model O_t
    # ----------------------------
    def observe(self):
        noise = np.random.randn(self.dim) * self.beta
        return self.true_state + noise

    # ----------------------------
    # Update field F(X, O, U)
    # Bayesian-like correction + control bias
    # ----------------------------
    def F(self, X, O, U):
        prediction_error = O - X
        return self.lr * prediction_error + self.alpha * U

    # ----------------------------
    # Noise term G dW_t
    # ----------------------------
    def G(self):
        return self.beta

    def noise(self):
        return np.random.randn(self.dim)

    # ----------------------------
    # Control policy U_t
    # (simple: move toward target = 0 or learned goal)
    # ----------------------------
    def control(self, X):
        target = np.zeros(self.dim)
        return target - X

    # ----------------------------
    # One step dynamics
    # ----------------------------
    def step(self, dt=1.0):
        O = self.observe()
        U = self.control(self.X)

        drift = self.F(self.X, O, U) * dt
        diffusion = self.G() * self.noise() * np.sqrt(dt)

        self.X = self.X + drift + diffusion

        return {
            "belief_state": self.X.copy(),
            "observation": O,
            "control": U
        }

    # ----------------------------
    # Simulation loop
    # ----------------------------
    def run(self, T=50, dt=1.0):
        trajectory = []

        for t in range(T):
            step_data = self.step(dt)
            trajectory.append(step_data)

        return trajectory


# ---------------------------------
# Example usage
# ---------------------------------
if __name__ == "__main__":
    system = BayesianControlDynamicalSystem(
        dim=1,
        alpha=0.6,
        beta=0.4,
        lr=0.2
    )

    traj = system.run(T=100)

    for i, s in enumerate(traj[:5]):
        print(f"Step {i}: X={s['belief_state']}, O={s['observation']}, U={s['control']}")
