# Figure 1C to plot software usage

import pandas as pd
import matplotlib.pyplot as plt
import re

# 1. Load the CSV dataset
file_path = 'MT.csv'
df = pd.read_csv(file_path)

# 2. Forward fill the 'Software' column to fill empty rows from parent entries
df['Software'] = df['Software'].ffill()

# 3. Function to count software tools per entry (delimited by commas or 'and')
def count_software(entry):
    if pd.isna(entry):
        return 0
    # Split on comma or the word 'and'
    tools = [tool.strip() for tool in re.split(r',|\band\b', str(entry)) if tool.strip()]
    return len(tools)

# Apply counting function
df['sw_count'] = df['Software'].apply(count_software)

# 4. Categorize counts into 1, 2, 3, and 4+
def categorize_count(count):
    if count == 1:
        return '1 program'
    elif count == 2:
        return '2 programs'
    elif count == 3:
        return '3 programs'
    elif count >= 4:
        return '4+ programs'
    return 'None'

df['category'] = df['sw_count'].apply(categorize_count)

# Filter out rows if software count is 0
df_valid = df[df['sw_count'] > 0]

# 5. Compute category frequencies
categories = ['1 program', '2 programs', '3 programs', '4+ programs']
counts = df_valid['category'].value_counts().reindex(categories, fill_value=0)

# 6. Plot the Pie Chart
plt.figure(figsize=(8, 6))
colors = ['#E69B00', '#55A868', '#C44E52', '#8172B8']

plt.pie(
    counts, 
    labels=counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)

plt.title('Distribution of Software Used for MT Reconstruction', fontsize=14, fontweight='bold')
plt.tight_layout()
#plt.show()

# Save the pie chart directly as a PDF file
plt.savefig('csMT_software_pie_chart.pdf', format='pdf', bbox_inches='tight')
plt.close()