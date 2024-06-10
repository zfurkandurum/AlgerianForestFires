import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
data = '''Day,Month,Year,Temperature,Relative Humidity,Wind Speed,Rain,Fine Fuel Moisture,Duff Moisture,Drought,Initial Spread,Buildup,Fire Weather,Fire Classes
01,06,2012,29,57,18,0,65.7,3.4,7.6,1.3,3.4,0.5,not fire
02,06,2012,29,61,13,1.3,64.4,4.1,7.6,1,3.9,0.4,not fire
... (the rest of your data)
'''

# Convert the string data into a DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Convert 'Fire Classes' to binary
df['Fire Classes'] = df['Fire Classes'].apply(lambda x: 1 if x.strip() == 'fire' else 0)

# Drop the first three columns
df = df.iloc[:, 3:]

# Generate histograms for each column
df.hist(bins=20, figsize=(15, 10))
plt.tight_layout()
plt.show()

# Calculate and print statistics
stats = df.describe()
print(stats)
