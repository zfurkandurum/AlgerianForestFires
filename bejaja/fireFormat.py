import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('algerian-bejaia.csv')

# Extract unique fire classes and their counts
fire_classes = df['Fire Classes'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
fire_classes.plot(kind='bar', color='skyblue')
plt.title('Fire Classes Distribution')
plt.xlabel('Fire Classes')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as PNG
plt.savefig('fire_classes_distribution.png')

# Show plot (optional)
plt.show()
