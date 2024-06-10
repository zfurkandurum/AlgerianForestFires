import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = 'algerian-bejaia.csv'
data = pd.read_csv(file_path)

# Generate histograms for each column
for column in data.columns:
    plt.figure()
    data[column].hist(bins=20)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
