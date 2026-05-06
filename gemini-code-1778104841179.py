!pip install qutip

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# 1. Defining the Bridge Constants
# Rust (Fe2O3) to Tungsten (W) Transition
# 252
SURFACE_POTENTIAL_RUST = 2.1  # eV
SURFACE_POTENTIAL_TUNGSTEN = 4.5 # eV
TIMESTEP = [2m] # Iterative scale reference

def simulate_bridge_flow():
    # 2. Quantum State Initialization
    # Ground state represents the Rust surface; excited state represents Tungsten
    basis_rust = basis(2, 0)
    basis_tungsten = basis(2, 1)
    
    # Initial state: Pure Rust
    psi0 = basis_rust
    
    # 3. Vector Flow Hamiltonian
    # Representing the flow across the bridge as a driven transition
    gamma = 0.5  # Coupling strength
    H = gamma * (sigmax() + sigmay()) 
    
    # 4. Optical Drive Storage Interaction
    # Simulating the pulse of an optical drive to store/retrieve state
    times = np.linspace(0, 10, 100)
    result = sesolve(H, psi0, times, [sigmax(), sigmay(), sigmaz()])
    
    return times, result.expect

# Execute Simulation
times, expectation = simulate_bridge_flow()

# 5. Visualizing the Vector Flow
plt.figure(figsize=(10, 5))
plt.plot(times, expectation[2], label='Rust-Tungsten Transition (Z-axis)')
plt.title("Quantum Bridge Vector Flow Simulation")
plt.xlabel("Time (Normalized)")
plt.ylabel("State Probability")
plt.grid(True)
plt.legend()
plt.show()