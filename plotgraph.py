import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Define the file name and color
file = 'reward_log'
color = '#e23bff'
#color = sns.color_palette('husl', 8)[7]
sns.set_style("ticks")
sns.set_context("talk")

# Read the data from the Excel file and skip the first row
df = pd.read_csv(file + '.csv', usecols=[0], skiprows=1)
transformed_data = df  # Transformation equation applied

# Find the last index where a datapoint is below 0
for i in range(len(df)-1):
        value = df.iloc[len(df)-1-i, 0]  # Assuming a single column DataFrame, adjust if necessary
        if value < 0:
            last_negative_index = len(df)-i
            break
            
# Convert index values to integers
last_negative_index = int(last_negative_index)

# Get the data points after the last negative point
data_after_last_negative = transformed_data.iloc[last_negative_index + 1:]

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
smooth_data = lowess(data_after_last_negative.values.flatten(), range(len(data_after_last_negative)), frac=0.02)  # smooth the data
ax.plot(range(len(smooth_data[:, 1])), smooth_data[:, 1], color=color, label=file, linewidth=2, alpha=1)  # plot the smoothed data

# Add labels and legend
ax.set_xlabel('Iterations')
ax.set_ylabel('Reward')
ax.set_title('Mean Rewards')

sns.despine(offset=1, trim=True)
plt.show()

