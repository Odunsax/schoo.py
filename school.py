import pandas as pd
import matplotlib.pyplot as plt

# Data for this year
current_year_data = {
    "Category": ["Accommodation/Admin Fees", "Transportation", "Feeding (Estimate)", "Total Cost"],
    "GVU (This Year)": [300000, 0, 60000, 360000],
    "KSU (This Year)": [100000, 30000, 60000, 190000],
}

# Data for next year
next_year_accommodation = 100000  # Next year's accommodation cost
other_estimate = 200000  # Estimate for other expenses next year
next_year_data = {
    "GVU (Next Year)": [
        next_year_accommodation,
        current_year_data["GVU (This Year)"][1],  # Transportation remains the same
        current_year_data["GVU (This Year)"][2],  # Feeding remains the same
        next_year_accommodation + current_year_data["GVU (This Year)"][1] +
        current_year_data["GVU (This Year)"][2] + other_estimate,
    ],
    "KSU (Next Year)": [
        next_year_accommodation,
        current_year_data["KSU (This Year)"][1],  # Transportation remains the same
        current_year_data["KSU (This Year)"][2],  # Feeding remains the same
        next_year_accommodation + current_year_data["KSU (This Year)"][1] +
        current_year_data["KSU (This Year)"][2] + other_estimate,
    ],
}

# Combine data into a DataFrame
df = pd.DataFrame(current_year_data)
df["GVU (Next Year)"] = next_year_data["GVU (Next Year)"]
df["KSU (Next Year)"] = next_year_data["KSU (Next Year)"]

# Calculate differences for total cost
df["Difference (This Year)"] = df["GVU (This Year)"] - df["KSU (This Year)"]
df["Difference (Next Year)"] = df["GVU (Next Year)"] - df["KSU (Next Year)"]

# Set the Category column as the index
df_display = df.set_index("Category")

# Plot bar chart
plt.figure(figsize=(12, 7))
categories = df["Category"][:-1]  # Exclude 'Total Cost' for detailed breakdown

# Bar chart for comparison
x = range(len(categories))
plt.bar(x, df["GVU (This Year)"][:-1], width=0.2, label="GVU (This Year)", align="center", color='blue')
plt.bar([i + 0.2 for i in x], df["KSU (This Year)"][:-1], width=0.2, label="KSU (This Year)", align="center", color='orange')
plt.bar([i + 0.4 for i in x], df["GVU (Next Year)"][:-1], width=0.2, label="GVU (Next Year)", align="center", color='green')
plt.bar([i + 0.6 for i in x], df["KSU (Next Year)"][:-1], width=0.2, label="KSU (Next Year)", align="center", color='red')

# Add labels and legend
plt.xticks([i + 0.3 for i in x], categories, rotation=45, ha="right")
plt.title("Cost Comparison: GVU vs KSU (This Year and Next Year)")
plt.ylabel("Cost (₦)")
plt.legend()
plt.tight_layout()
plt.show()

# Display the updated DataFrame
print(df_display)

# Pie chart for GVU and KSU cost distribution (Next Year)
plt.figure(figsize=(12, 6))

# Subplot for GVU (Next Year)
plt.subplot(1, 2, 1)
plt.pie(
    next_year_data["GVU (Next Year)"][:-1],  # Exclude Total Cost
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=['skyblue', 'lightgreen', 'lightcoral']
)
plt.title("GVU Cost Distribution (Next Year)")

# Subplot for KSU (Next Year)
plt.subplot(1, 2, 2)
plt.pie(
    next_year_data["KSU (Next Year)"][:-1],  # Exclude Total Cost
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=['gold', 'tomato', 'lightpink']
)
plt.title("KSU Cost Distribution (Next Year)")

plt.tight_layout()
plt.show()
