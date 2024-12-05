import pandas as pd
import matplotlib.pyplot as plt

# Data for analysis
data = {
    "Category": ["Accommodation/Admin Fees", "Transportation", "Feeding (Estimate)", "Total Cost"],
    "GVU": [300000, 0, 60000, 360000],  # Feeding estimated at 60k/year pay-as-you-eat
    "KSU": [100000, 30000, 60000, 190000],  # Estimated values for public university expenses
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate total costs
df["Difference"] = df["GVU"] - df["KSU"]

# Display the table
df_display = df.set_index("Category")

# Plotting
plt.figure(figsize=(10, 6))
categories = df["Category"][:-1]  # Exclude 'Total Cost' for detailed breakdown

# Bar chart for comparison
x = range(len(categories))
plt.bar(x, df["GVU"][:-1], width=0.4, label="GVU", align="center", color='blue')
plt.bar([i + 0.4 for i in x], df["KSU"][:-1], width=0.4, label="KSU", align="center", color='orange')

# Add labels and legend
plt.xticks([i + 0.2 for i in x], categories, rotation=45, ha="right")
plt.title("Cost Comparison: GVU vs KSU")
plt.ylabel("Cost (₦)")
plt.legend()
plt.tight_layout()

plt.show()

# Display the DataFrame
print(df_display)
