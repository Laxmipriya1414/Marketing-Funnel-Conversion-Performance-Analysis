import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("marketing_data.csv")

print("\nMarketing Funnel Dataset")
print(df)

# KPIs
total_leads = df["Leads"].sum()
total_customers = df["Customers"].sum()
total_revenue = df["Revenue"].sum()

overall_conversion = (total_customers / total_leads) * 100

print("\n========== KPIs ==========")
print(f"Total Leads: {total_leads}")
print(f"Total Customers: {total_customers}")
print(f"Total Revenue: ${total_revenue}")
print(f"Overall Conversion Rate: {overall_conversion:.2f}%")

# Conversion Rate by Channel
df["Conversion Rate"] = (df["Customers"] / df["Leads"]) * 100

# Chart 1
plt.figure(figsize=(8,5))
plt.bar(df["Channel"], df["Conversion Rate"])
plt.title("Conversion Rate by Channel")
plt.xlabel("Channel")
plt.ylabel("Conversion Rate (%)")
plt.tight_layout()
plt.savefig("charts/channel_conversion.png")
plt.close()

# Chart 2
plt.figure(figsize=(8,5))
plt.bar(df["Channel"], df["Revenue"])
plt.title("Revenue by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/revenue_by_channel.png")
plt.close()

# Funnel Stages
stages = [
    df["Leads"].sum(),
    df["Qualified Leads"].sum(),
    df["Opportunities"].sum(),
    df["Customers"].sum()
]

labels = ["Leads","Qualified","Opportunities","Customers"]

plt.figure(figsize=(8,5))
plt.plot(labels, stages, marker="o")
plt.title("Marketing Funnel")
plt.grid(True)
plt.savefig("charts/funnel_stages.png")
plt.close()

# Drop-Off Analysis
drop_off = [
    stages[0]-stages[1],
    stages[1]-stages[2],
    stages[2]-stages[3]
]

drop_labels = [
    "Lead → Qualified",
    "Qualified → Opportunity",
    "Opportunity → Customer"
]

plt.figure(figsize=(8,5))
plt.bar(drop_labels, drop_off)
plt.title("Customer Drop-Off Analysis")
plt.tight_layout()
plt.savefig("charts/dropoff_analysis.png")
plt.close()

# Leads vs Customers
plt.figure(figsize=(8,5))
plt.plot(df["Channel"], df["Leads"], marker="o", label="Leads")
plt.plot(df["Channel"], df["Customers"], marker="o", label="Customers")
plt.legend()
plt.title("Leads vs Customers")
plt.tight_layout()
plt.savefig("charts/leads_vs_customers.png")
plt.close()

print("\nAnalysis Completed Successfully!")
print("Charts saved in charts folder.")