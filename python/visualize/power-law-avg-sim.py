import numpy as np
import matplotlib.pyplot as plt

def simulate_st_petersburg(n_games):
    # Simulate n_games
    # np.random.geometric(p=0.5) returns the number of trials to get the first success (Tail).
    # If the result is k, it means (k-1) Heads and then 1 Tail.
    # The payout is 2^k.
    tosses = np.random.geometric(p=0.5, size=n_games)
    
    # Calculate payouts
    # We use float to avoid integer overflow for very lucky runs, though rare.
    payouts = 2.0 ** tosses
    
    # Calculate running average (cumulative sum / count)
    cumulative_payouts = np.cumsum(payouts)
    game_indices = np.arange(1, n_games + 1)
    running_averages = cumulative_payouts / game_indices
    
    return running_averages

# Parameters
n_games = 100000  # Number of games to play in one simulation
n_simulations = 5 # Number of different simulations to overlay

plt.figure(figsize=(12, 6))

# Run simulations and plot
for i in range(n_simulations):
    avg_payouts = simulate_st_petersburg(n_games)
    plt.plot(avg_payouts, label=f'Simulation {i+1}', alpha=0.8, linewidth=1)

# Theoretical Reference (optional, but since mean is infinity, we can't plot it. 
# instead, we plot log2(n) which is often discussed as a "fair" entry fee in finite games)
# x_vals = np.arange(1, n_games + 1)
# plt.plot(x_vals, 0.5 * np.log2(x_vals), 'k--', label='0.5 * log2(n)', alpha=0.5)

plt.title('St. Petersburg Paradox: Running Average of Payouts\n(Mean does not converge)', fontsize=14)
plt.xlabel('Number of Games (n)', fontsize=12)
plt.ylabel('Average Payout ($)', fontsize=12)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.4)

# Use a log scale for x-axis to better see the behavior across orders of magnitude?
# The prompt asks for "change with rounds". Linear is often more intuitive for "time", 
# but log x allows seeing early volatility vs late stability. 
# Let's keep linear X to show the "shocks".
plt.xscale('linear') 

plt.tight_layout()
plt.savefig('st_petersburg_simulation.png')