import matplotlib.pyplot as plt
import pandas as pd

# Note: Ensure df_A and df_B are defined or imported in your environment
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Algorithm A
axes[0].plot(
    df_A['n'], df_A['calls'], marker='o', color='darkred', label='Algorithm A'
)
axes[0].set_yscale('log')
axes[0].set_title('Algorithm A: Calls vs n (Log Scale)')
axes[0].set_xlabel('n')
axes[0].set_ylabel('Calls (log scale)')
axes[0].grid(True, which='both', linestyle='--', alpha=0.5)
axes[0].legend()

# Subplot 2: Algorithm A vs B Comparison
axes[1].plot(
    df_A['n'], df_A['calls'], marker='o', color='darkred', label='Algorithm A'
)
axes[1].plot(
    df_B['n'], df_B['calls'], marker='s', color='navy', label='Algorithm B'
)
axes[1].set_yscale('log')
axes[1].set_title('Comparison: Algorithm A vs. Algorithm B')
axes[1].set_xlabel('n')
axes[1].set_ylabel('Calls (log scale)')
axes[1].grid(True, which='both', linestyle='--', alpha=0.5)
axes[1].legend()

plt.tight_layout()
plt.savefig('fibonacci_calls_plot.png', dpi=300)
plt.show()