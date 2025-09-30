import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create sample population data
np.random.seed(42)  # for reproducibility
n_countries = 200
population_sizes = np.concatenate([
    np.random.normal(1e6, 5e5, n_countries//2),  # Small countries
    np.random.normal(50e6, 20e6, n_countries//2)  # Large countries
])

# Create a DataFrame
df = pd.DataFrame({
    'Country': [f'Country_{i}' for i in range(n_countries)],
    'Population': population_sizes
})

# Create the histogram
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Population', bins=30)

# Customize the plot
plt.title('Distribution of Population Across Countries (Sample Data)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')

# Use scientific notation for x-axis
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Improve the layout
plt.tight_layout()

# Show the plot
plt.show()