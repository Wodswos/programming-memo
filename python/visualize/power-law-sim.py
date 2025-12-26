import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def simulate_distribution(n_games, multiplier):
    # Simulate geometric distribution (number of trials to get first success)
    k_values = np.random.geometric(p=0.5, size=n_games)
    
    # Calculate payoffs
    # using float to handle potentially large numbers for plotting
    payoffs = np.power(multiplier, k_values - 1).astype(np.float64)
    
    # Count frequency of each unique payoff
    # We use Counter to get exact counts of discrete outcomes
    counts = Counter(payoffs)
    
    # Sort by payoff amount
    sorted_payoffs = sorted(counts.keys())
    frequencies = [counts[val] for val in sorted_payoffs]
    probabilities = [f / n_games for f in frequencies]
    
    return sorted_payoffs, probabilities

# Parameters
n_simulations = 100000000  # 1 million runs for better tail resolution

# Run simulations
payoffs_2, probs_2 = simulate_distribution(n_simulations, 2)
payoffs_1_5, probs_1_5 = simulate_distribution(n_simulations, 1.5)

# Setup the plot
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Standard Bar Chart (First 10 outcomes) - To show the immediate reality
# We limit to first 10 to keep it readable
limit = 10
labels_2 = [f"{p:.0f}" for p in payoffs_2[:limit]]
axes[0].bar(range(limit), probs_2[:limit], color='tab:blue', alpha=0.7, label='Multiplier=2')
axes[0].set_xticks(range(limit))
axes[0].set_xticklabels(labels_2)
axes[0].set_title(f'Probability of First {limit} Outcomes (Multiplier=2)')
axes[0].set_xlabel('Payoff Amount ($)')
axes[0].set_ylabel('Probability')
axes[0].grid(axis='y', alpha=0.3)

# Plot 2: Log-Log Plot (The Power Law) - To show the tail
axes[1].scatter(payoffs_2, probs_2, color='tab:blue', alpha=0.6, label='Multiplier = 2 (Slope $\\approx$ -1)', s=15)
axes[1].scatter(payoffs_1_5, probs_1_5, color='tab:green', alpha=0.6, label='Multiplier = 1.5 (Steeper Slope)', s=15)

axes[1].set_xscale('log')
axes[1].set_yscale('log')
axes[1].set_title('Payoff Distribution (Log-Log Scale)')
axes[1].set_xlabel('Payoff Amount ($) - Log Scale')
axes[1].set_ylabel('Probability - Log Scale')
axes[1].grid(True, which="both", ls="-", alpha=0.2)
axes[1].legend()

plt.savefig('distribution_plot.png')

# Prepare a summary table for the user
df_2 = pd.DataFrame({'Payoff': payoffs_2, 'Probability': probs_2})
df_1_5 = pd.DataFrame({'Payoff': payoffs_1_5, 'Probability': probs_1_5})

print("Top 5 most common outcomes for Multiplier=2:")
print(df_2.head(5))
print("\nTop 5 rarest outcomes encountered for Multiplier=2 (Tail):")
print(df_2.tail(5))