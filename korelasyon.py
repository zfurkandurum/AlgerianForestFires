import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('algerian-bejaia.csv')

# Exclude non-numeric columns
numeric_data = data.drop(columns=data.columns[[0, 1, 2, -1]])  # Adjust index positions as needed

# Calculate correlation matrix
correlation_matrix = numeric_data.corr()

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)

# Add title and rotate y-axis labels
plt.title('Correlation Matrix of Numeric Features')
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.tight_layout()

# Save the heatmap as a PNG file
plt.savefig('correlation_matrix.png')

# Show plot
plt.show()
