import numpy as np
import matplotlib.pyplot as plt

# Simulated data for journey times before and after closure
# We'll create a normal distribution centered around the mean journey times
np.random.seed(0)  # For reproducibility

# Simulate pre-shutdown times with a smaller standard deviation
pre_shutdown_times = np.random.normal(loc=80.04, scale=5, size=1000)

# Simulate post-shutdown times with a larger standard deviation
post_shutdown_times = np.random.normal(loc=96.84, scale=10, size=1000)

def plot_journey_times_histogram(pre_times, post_times):
    plt.figure(figsize=(10, 5))

    # Histogram for pre-shutdown times
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
    plt.hist(pre_times, bins=30, color='blue', alpha=0.7)
    plt.title('Pre-Shutdown Journey Times')
    plt.xlabel('Journey Time (minutes)')
    plt.ylabel('Frequency')

    # Histogram for post-shutdown times
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
    plt.hist(post_times, bins=30, color='red', alpha=0.7)
    plt.title('Post-Shutdown Journey Times')
    plt.xlabel('Journey Time (minutes)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

plot_journey_times_histogram(pre_shutdown_times, post_shutdown_times)
